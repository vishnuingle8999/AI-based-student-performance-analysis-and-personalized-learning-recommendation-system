import sys
import os
import unittest
import json

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models.schema import (
    db, Student, Branch, Semester, Subject, Topic, Question, TestAttempt, LearningResource
)
from ml.resource_ranking import (
    rank_resources_for_topic,
    score_resource,
    extract_youtube_embed_url,
    generate_fallback_search_links
)

class TestPersonalizedPreferencesAndResources(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    # -------------------------------------------------------------------------
    # 1. Learning Preferences Tests
    # -------------------------------------------------------------------------
    def test_default_preference_for_new_student(self):
        """Verify new students receive 'both' as their default learning preference."""
        new_student_id = "TEST_PREF_NEW"
        existing = Student.query.filter_by(student_id=new_student_id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()

        sem = Semester.query.first()
        res = self.client.post('/register', data={
            'student_id': new_student_id,
            'name': 'Test Preference Student',
            'email': 'pref_test@college.edu',
            'password': 'password123',
            'branch_id': sem.branch_id,
            'year_id': sem.year_id,
            'semester_id': sem.id
            # Notice learning_preference omitted to test default
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        created = Student.query.filter_by(student_id=new_student_id).first()
        self.assertIsNotNone(created, "Student should be registered")
        self.assertEqual(created.learning_preference, 'both', "Default preference must be 'both'")

        # Clean up
        db.session.delete(created)
        db.session.commit()

    def test_preference_update_and_persistence(self):
        """Verify student can change preference to 'notes', 'videos', and 'both' and choice persists."""
        # Login demo student S001
        self.client.post('/login', data={'login_identifier': 'S001', 'password': 'password123'})

        # Update to 'videos'
        res = self.client.post('/preferences/update', data={'learning_preference': 'videos'}, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        s001 = Student.query.filter_by(student_id='S001').first()
        self.assertEqual(s001.learning_preference, 'videos')

        # Logout and re-login, verify persistence
        self.client.get('/logout')
        s001_check = Student.query.filter_by(student_id='S001').first()
        self.assertEqual(s001_check.learning_preference, 'videos', "Preference must persist in database after logout")

        self.client.post('/login', data={'login_identifier': 'S001', 'password': 'password123'})
        # Update to 'notes'
        res = self.client.post('/preferences/update', data={'learning_preference': 'notes'}, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        s001 = Student.query.filter_by(student_id='S001').first()
        self.assertEqual(s001.learning_preference, 'notes')

        # Reset back to 'both'
        self.client.post('/preferences/update', data={'learning_preference': 'both'}, follow_redirects=True)
        s001 = Student.query.filter_by(student_id='S001').first()
        self.assertEqual(s001.learning_preference, 'both')

    def test_invalid_preference_rejected(self):
        """Ensure invalid preference values are safely rejected by server-side validation."""
        self.client.post('/login', data={'login_identifier': 'S001', 'password': 'password123'})
        res = self.client.post('/preferences/update', data={'learning_preference': 'invalid_mode'}, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Invalid learning preference option", res.data)
        s001 = Student.query.filter_by(student_id='S001').first()
        self.assertIn(s001.learning_preference, ['notes', 'videos', 'both'])

    def test_profile_updates_learning_preference(self):
        """Verify profile form also allows updating learning preference."""
        self.client.post('/login', data={'login_identifier': 'S001', 'password': 'password123'})
        s001 = Student.query.filter_by(student_id='S001').first()
        res = self.client.post('/profile', data={
            'branch_id': s001.branch_id,
            'year_id': s001.year_id,
            'semester_id': s001.semester_id,
            'learning_preference': 'notes'
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        s001 = Student.query.filter_by(student_id='S001').first()
        self.assertEqual(s001.learning_preference, 'notes')
        # Reset back to both
        s001.learning_preference = 'both'
        db.session.commit()

    # -------------------------------------------------------------------------
    # 2. Multi-Platform Educational Resources Database Tests
    # -------------------------------------------------------------------------
    def test_educational_resources_seeded_and_platforms_present(self):
        """Verify database contains curated resources across multiple platforms."""
        total_res = LearningResource.query.count()
        self.assertGreaterEqual(total_res, 50, f"Expected at least 50 curated educational resources, found {total_res}")

        # Check for GeeksforGeeks
        gfg_count = LearningResource.query.filter(LearningResource.provider.like('%GeeksforGeeks%')).count()
        self.assertGreater(gfg_count, 10, "GeeksforGeeks resources must be present")

        # Check for Video resources (YouTube videos from freeCodeCamp, StatQuest, 3Blue1Brown, NPTEL, etc.)
        video_count = LearningResource.query.filter_by(resource_type='video').count()
        self.assertGreater(video_count, 10, "Video resources must be present")

        # Check for Documentation
        docs_count = LearningResource.query.filter_by(resource_type='documentation').count()
        self.assertGreater(docs_count, 5, "Official documentation resources must be present")

    def test_youtube_embed_url_extraction(self):
        """Verify YouTube watch URLs are safely converted into embed URLs with privacy enhancements."""
        url1 = "https://www.youtube.com/watch?v=aircAruvnKk"
        embed1 = extract_youtube_embed_url(url1)
        self.assertEqual(embed1, "https://www.youtube-nocookie.com/embed/aircAruvnKk")

        url2 = "https://youtu.be/Gv9_4yMHFhI"
        embed2 = extract_youtube_embed_url(url2)
        self.assertEqual(embed2, "https://www.youtube-nocookie.com/embed/Gv9_4yMHFhI")

        non_yt = "https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"
        self.assertEqual(extract_youtube_embed_url(non_yt), "")

    # -------------------------------------------------------------------------
    # 3. Intelligent Ranking Engine Tests
    # -------------------------------------------------------------------------
    def test_ranking_when_preference_is_notes(self):
        """When student selects 'notes', theory articles and notes must rank first."""
        # Find a topic with multiple resources
        topic = Topic.query.filter(Topic.resources.any()).first()
        self.assertIsNotNone(topic)
        resources = LearningResource.query.filter_by(topic_id=topic.id).all()
        self.assertGreater(len(resources), 1)

        ranked = rank_resources_for_topic(
            resources=resources,
            student_preference='notes',
            topic_accuracy=30.0,
            topic_name=topic.name
        )
        self.assertGreater(len(ranked), 0)
        # First resource must be notes / documentation
        self.assertIn(ranked[0]['resource_type'], ['notes', 'documentation'], "Top resource must be notes/docs when preference='notes'")
        self.assertIn("preference", ranked[0]['recommendation_reason'].lower())

    def test_ranking_when_preference_is_videos(self):
        """When student selects 'videos', video lectures must rank first."""
        topic = Topic.query.filter(Topic.resources.any()).first()
        resources = LearningResource.query.filter_by(topic_id=topic.id).all()

        ranked = rank_resources_for_topic(
            resources=resources,
            student_preference='videos',
            topic_accuracy=30.0,
            topic_name=topic.name
        )
        self.assertGreater(len(ranked), 0)
        self.assertEqual(ranked[0]['resource_type'], 'video', "Top resource must be video when preference='videos'")
        self.assertIn("video", ranked[0]['recommendation_reason'].lower())

    def test_ranking_when_preference_is_both(self):
        """When student selects 'both', notes and video lectures are ranked together by educational fit."""
        topic = Topic.query.filter(Topic.resources.any()).first()
        resources = LearningResource.query.filter_by(topic_id=topic.id).all()

        ranked = rank_resources_for_topic(
            resources=resources,
            student_preference='both',
            topic_accuracy=25.0,  # WEAK -> beginner priority
            topic_name=topic.name
        )
        self.assertGreater(len(ranked), 0)
        types = [r['resource_type'] for r in ranked]
        self.assertTrue('notes' in types or 'documentation' in types)
        self.assertTrue('video' in types)
        # Beginner resource should score higher for low accuracy
        self.assertEqual(ranked[0]['difficulty'], 'Beginner')

    def test_fallback_search_links_generation(self):
        """Verify topic-specific search queries are generated correctly."""
        fallbacks = generate_fallback_search_links("Linear Regression", "Machine Learning", "both")
        self.assertIn("gfg_search", fallbacks)
        self.assertIn("youtube_search", fallbacks)
        self.assertIn("nptel_search", fallbacks)
        self.assertIn("docs_search", fallbacks)
        self.assertIn("Linear+Regression", fallbacks['gfg_search'])
        self.assertIn("youtube.com/results", fallbacks['youtube_search'])

    # -------------------------------------------------------------------------
    # 4. Admin Resource Management & Authorization Tests
    # -------------------------------------------------------------------------
    def test_admin_can_add_toggle_and_delete_resource(self):
        """Verify admin can add, verify/unverify, and delete resources."""
        self.client.post('/login', data={'login_identifier': 'admin@college.edu', 'password': 'admin123'})

        topic = Topic.query.first()
        self.assertIsNotNone(topic)

        # Add resource
        res = self.client.post('/admin/add-resource', data={
            'topic_id': topic.id,
            'title': 'Test Integration Resource for AI',
            'provider': 'GeeksforGeeks',
            'resource_type': 'notes',
            'resource_url': 'https://www.geeksforgeeks.org/artificial-intelligence-an-introduction/',
            'description': 'Integration test resource',
            'language': 'English',
            'difficulty': 'Beginner',
            'verification_status': 'verified'
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        created = LearningResource.query.filter_by(title='Test Integration Resource for AI').first()
        self.assertIsNotNone(created, "Resource should be created in database")
        self.assertEqual(created.verification_status, 'verified')

        # Toggle verify
        res = self.client.post(f'/admin/toggle-verify-resource/{created.id}', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        created = db.session.get(LearningResource, created.id)
        self.assertEqual(created.verification_status, 'unverified')

        # Toggle back to verified
        res = self.client.post(f'/admin/toggle-verify-resource/{created.id}', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        created = db.session.get(LearningResource, created.id)
        self.assertEqual(created.verification_status, 'verified')

        # Delete resource
        res = self.client.post(f'/admin/delete-resource/{created.id}', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        deleted = db.session.get(LearningResource, created.id)
        self.assertIsNone(deleted, "Resource should be deleted")

    def test_non_admin_cannot_manage_resources(self):
        """Ensure standard students cannot add, delete, or toggle resources."""
        self.client.get('/logout')
        self.client.post('/login', data={'login_identifier': 'S001', 'password': 'password123'})

        topic = Topic.query.first()
        res = self.client.post('/admin/add-resource', data={
            'topic_id': topic.id,
            'title': 'Unauthorized Resource',
            'provider': 'Malicious',
            'resource_url': 'https://example.com'
        }, follow_redirects=True)
        self.assertIn(b"Administrator privileges required", res.data)
        unauth = LearningResource.query.filter_by(title='Unauthorized Resource').first()
        self.assertIsNone(unauth)

    # -------------------------------------------------------------------------
    # 5. UI Integration & Recommendations View Tests
    # -------------------------------------------------------------------------
    def test_recommendations_page_renders_learning_preferences_and_resources(self):
        """Verify the recommendations template renders preference switcher and resource cards."""
        self.client.post('/login', data={'login_identifier': 'S001', 'password': 'password123'})
        res = self.client.get('/recommendations')
        self.assertEqual(res.status_code, 200)

        # Check Preference bar elements
        self.assertIn(b"Your Learning Method Preference", res.data)
        self.assertIn(b"Option 1: Theory Notes", res.data)
        self.assertIn(b"Option 2: Video Lectures", res.data)
        self.assertIn(b"Option 3: Both Notes", res.data)
        self.assertIn(b"Save Learning Preference", res.data)

        # Check Video Modal
        self.assertIn(b"id=\"videoModal\"", res.data)
        self.assertIn(b"videoIframe", res.data)

        # Check curated learning resources rendered
        self.assertIn(b"Curated Learning Resources", res.data)
        self.assertIn(b"Direct Topic Search Options", res.data)


if __name__ == '__main__':
    unittest.main()
