# -*- coding: utf-8 -*-
"""
Generate 240 DBATU Questions for Semester IV (60 questions for each of the 4 subjects)
Subjects:
  1. Introduction to Operating Systems (25AFAIPC401) - 60 Qs
  2. Data Analytics (25AFAIPC402) - 60 Qs
  3. Probability and Statistics (25AF1245PC403) - 60 Qs
  4. Full Stack Development (25AFAIPCL404) - 60 Qs
"""

def get_os_questions():
    questions = []
    sub = "Introduction to Operating Systems"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester IV"

    u1 = "Unit 1: Introduction and Operating System Structures"
    t1 = "Operating System Structures & System Calls"
    os_u1 = [
        (t1, "What is the primary role of an Operating System as an extended machine / resource allocator?",
         "Compiling high-level programming code into bytecode",
         "Managing hardware resources (CPU, memory, I/O) and providing an abstract API to user applications",
         "Providing power supply to motherboards", "Formatting optical discs", "B", "Easy"),
        (t1, "Which of the following is an example of a hard Real-Time Operating System (RTOS)?",
         "Windows 11", "VxWorks / FreeRTOS", "Ubuntu Desktop", "macOS Sonoma", "B", "Medium"),
        (t1, "What mechanism allows a user-mode application to safely request privileged services from the OS kernel?",
         "System Call (via software interrupt / trap)", "Direct memory bus write", "Unchecked pointer dereference", "Standard HTTP request", "A", "Easy"),
        (t1, "Which CPU privilege mode executes user application programs to protect critical hardware registers?",
         "Kernel Mode (Supervisor Mode)", "User Mode (Ring 3)", "Hypervisor Ring -1", "Firmware BIOS Mode", "B", "Easy"),
        (t1, "In a Monolithic Kernel architecture (like Linux):",
         "All core OS services (VFS, IPC, drivers, scheduling) run in a single large address space in kernel mode",
         "Only basic IPC runs in kernel mode; drivers run as user processes",
         "There is no kernel mode", "Only 1 process can run at a time", "A", "Medium"),
        (t1, "In a Microkernel architecture (like Mach or QNX), how do system components typically communicate?",
         "Through shared physical registers without checks", "Via message passing through the microkernel IPC mechanism",
         "By compiling into a single executable", "Through optical cables", "B", "Medium"),
        (t1, "Which system call in UNIX creates a new child process as an exact duplicate of the parent process?",
         "fork()", "exec()", "wait()", "exit()", "A", "Easy"),
        (t1, "What happens when the exec() system call is invoked in a newly created process?",
         "It terminates the parent process", "It replaces the current process address space with a new program binary",
         "It duplicates the process again", "It allocates a swap file", "B", "Medium"),
        (t1, "Which system call causes a parent process to suspend execution until one of its child processes terminates?",
         "sleep()", "wait() / waitpid()", "yield()", "kill()", "B", "Easy"),
        (t1, "What is a 'Dual-Mode Operation' in modern processors designed to protect the operating system from errant users?",
         "User Mode and Kernel (Privileged) Mode controlled by a hardware Mode Bit",
         "AC power mode and Battery power mode", "Single core and Dual core execution", "ASCII and Unicode mode", "A", "Medium"),
        (t1, "Which data structure maintained by the OS stores complete information about a specific process (PID, state, registers, memory limits)?",
         "Process Control Block (PCB)", "File Allocation Table (FAT)", "Inverted Page Table", "Inode descriptor", "A", "Easy"),
        (t1, "What is a 'Virtual Machine' in system structure taxonomy?",
         "A purely mechanical computing device", "An emulation of a computer system providing hardware functionality of a physical machine",
         "A local loopback network adapter", "A screen saver", "B", "Easy")
    ]

    u2 = "Unit 2: Processes and CPU Scheduling"
    t2 = "Processes, Threads & CPU Scheduling"
    os_u2 = [
        (t2, "What is the primary difference between a process and a thread?",
         "A process has its own isolated address space; threads within the same process share code, data, and resources but have their own stack and registers",
         "A process runs faster than a thread", "A thread cannot perform calculations", "Processes share a single stack", "A", "Easy"),
        (t2, "Which process state transition occurs when the CPU scheduler picks a process from the Ready queue to execute on the CPU?",
         "Running to Waiting", "Ready to Running (Dispatch)", "New to Terminated", "Waiting to Ready", "B", "Easy"),
        (t2, "What is 'Context Switching' overhead in operating systems?",
         "The time taken to save the state of the currently executing process/thread and restore the state of the next scheduled process",
         "The time taken to power off the machine", "The duration of an internet download", "The delay of typing on a keyboard", "A", "Medium"),
        (t2, "Which non-preemptive CPU scheduling algorithm suffers from the 'Convoy Effect' when a long CPU-burst process arrives first?",
         "Shortest Job First (SJF)", "First-Come, First-Served (FCFS)", "Round Robin (RR)", "Multi-Level Feedback Queue", "B", "Easy"),
        (t2, "Which CPU scheduling algorithm gives the minimum average waiting time for a given set of processes?",
         "FCFS", "Shortest Job First (SJF) / Shortest Remaining Time First (SRTF)", "Priority Scheduling", "Lottery Scheduling", "B", "Medium"),
        (t2, "In Round Robin (RR) CPU scheduling, what happens if the time quantum is chosen to be extremely large (larger than the longest burst)?",
         "RR degenerates into FCFS scheduling", "Context switching frequency increases to infinity",
         "Processes execute simultaneously without time limits", "The system deadlocks", "A", "Medium"),
        (t2, "In Round Robin scheduling, what happens if the time quantum is extremely small (e.g. 1 microsecond)?",
         "Processor throughput reaches 100%", "Context switching overhead dominates, severely degrading CPU efficiency",
         "SJF behavior is achieved", "All processes finish in 1 second", "B", "Medium"),
        (t2, "What is 'Starvation' in priority-based CPU scheduling algorithms?",
         "When high-priority processes run continuously, preventing low-priority processes from ever acquiring the CPU",
         "When the computer runs out of physical RAM", "When the disk write head gets stuck", "When CPU temperature exceeds limits", "A", "Easy"),
        (t2, "Which technique solves process starvation by gradually increasing the priority of processes that wait in the system for long periods?",
         "Paging", "Aging", "Compaction", "Swapping", "B", "Easy"),
        (t2, "In Multilevel Feedback Queue (MLFQ) scheduling, how are processes dynamically prioritized?",
         "Processes that use too much CPU time are moved to lower-priority queues; I/O-bound processes are kept in higher-priority queues",
         "Processes are sorted strictly by process name length", "All queues have identical time slices", "User processes override kernel processes", "A", "Hard"),
        (t2, "What is a 'Zombie Process' in UNIX systems?",
         "A process that has finished execution via exit() but still has an entry in the process table because its parent has not yet called wait()",
         "A process with infinite loop recursion", "A malicious trojan horse", "A process running on a remote cluster", "A", "Medium"),
        (t2, "What is an 'Orphan Process' in UNIX?",
         "A running process whose original parent process has terminated before calling wait() (re-parented to init/systemd with PID 1)",
         "A thread that has crashed", "A file without an owner", "A corrupted disk sector", "A", "Medium")
    ]

    u3 = "Unit 3: Process Synchronization and Deadlocks"
    t3 = "Synchronization & Deadlock Prevention"
    os_u3 = [
        (t3, "What is a 'Race Condition' in concurrent programming?",
         "A competition between hardware manufacturers",
         "A situation where multiple concurrent threads access and manipulate shared data, and the final outcome depends on the execution order",
         "A fast CPU scheduling algorithm", "A benchmark test for network bandwidth", "B", "Easy"),
        (t3, "What three requirements must any valid solution to the Critical Section problem satisfy?",
         "Mutual Exclusion, Progress, and Bounded Waiting", "Speed, Accuracy, and Low Memory",
         "Atomicity, Consistency, and Durability", "Encryption, Authentication, and Non-repudiation", "A", "Medium"),
        (t3, "What is a 'Semaphore' in process synchronization?",
         "A hardware graphics card", "An integer variable accessed only through atomic wait() [P] and signal() [V] operations",
         "A network packet sniffer", "A database query language", "B", "Easy"),
        (t3, "What is the difference between a Counting Semaphore and a Binary Semaphore (Mutex)?",
         "Counting semaphore values can range over an unrestricted integer domain to control access to finite resources; Binary semaphore value is 0 or 1",
         "Counting semaphores are for threads; binary semaphores are for hard drives",
         "Binary semaphores are non-atomic", "There is no functional difference", "A", "Easy"),
        (t3, "What classic synchronization problem models producer threads writing data into a fixed-size buffer and consumer threads reading from it?",
         "Dining Philosophers Problem", "Bounded-Buffer (Producer-Consumer) Problem", "Readers-Writers Problem", "Sleeping Barber Problem", "B", "Easy"),
        (t3, "Which four Coffman conditions must hold simultaneously for a Deadlock to occur?",
         "Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait",
         "Read, Write, Execute, Delete", "Paging, Segmentation, Swapping, Compaction", "Authentication, Authorization, Accounting, Auditing", "A", "Medium"),
        (t3, "Which deadlock handling algorithm developed by Edsger Dijkstra tests for safety before granting resource requests?",
         "Banker's Algorithm", "Kruskal's Algorithm", "Peterson's Algorithm", "Dijkstra's Shortest Path", "A", "Medium"),
        (t3, "In the Banker's Algorithm, what defines a 'Safe State'?",
         "A state where all processes are terminated",
         "A state where there exists at least one safe execution sequence of processes that can finish without causing a deadlock",
         "A state where CPU utilization is 0%", "A state where memory is fully encrypted", "B", "Hard"),
        (t3, "How does the OS recover from an already detected deadlock in system resources?",
         "Terminating one or more deadlocked processes, or preempting resources from processes until circular wait is broken",
         "Re-installing the operating system", "Turning off the monitor", "Changing the network IP address", "A", "Easy"),
        (t3, "What is 'Peterson's Solution' in operating system theory?",
         "A classic software-based two-process synchronization algorithm that guarantees mutual exclusion using turn and flag variables",
         "A disk scheduling algorithm", "A page replacement policy", "A file compression format", "A", "Medium"),
        (t3, "What hardware atomic instruction is commonly supported by modern CPUs to implement mutual exclusion spinlocks?",
         "Test-And-Set (or Compare-And-Swap)", "NOP (No Operation)", "JUMP unconditional", "ADD immediate", "A", "Medium"),
        (t3, "What is a 'Monitor' in programming languages (such as Java)?",
         "A physical display screen", "A high-level synchronization construct encapsulating shared variables and procedures with implicit mutual exclusion",
         "A network firewall log watcher", "A virus scanner", "B", "Medium")
    ]

    u4 = "Unit 4: Memory Management and Virtual Memory"
    t4 = "Memory Allocation & Page Replacement"
    os_u4 = [
        (t4, "What is the difference between a Logical (Virtual) Address and a Physical Address?",
         "Logical address is generated by the CPU during program execution; Physical address is the actual location in physical RAM loaded into the Memory Address Register",
         "Physical address is generated by software; logical address is the RAM hardware chip",
         "Logical address is measured in megahertz; physical address in gigahertz", "Both addresses are identical on all modern systems", "A", "Easy"),
        (t4, "What hardware component translates virtual memory addresses to physical memory addresses at runtime?",
         "Memory Management Unit (MMU)", "Arithmetic Logic Unit (ALU)", "Direct Memory Access (DMA) Controller", "Graphics Processing Unit (GPU)", "A", "Easy"),
        (t4, "What is 'Internal Fragmentation' in contiguous memory allocation?",
         "Unused memory scattered between allocated memory partitions",
         "Unused allocated memory space inside a partition or page that exceeds the memory required by the process",
         "A broken hard drive sector", "Corrupted CPU registers", "B", "Medium"),
        (t4, "What is 'External Fragmentation' in variable-partition memory allocation?",
         "Total free memory space is sufficient to satisfy a request, but it is fragmented into non-contiguous blocks too small to accommodate the process",
         "Unused space within a 4KB page", "Damage to RAM chips", "A virus infection in system swap", "A", "Medium"),
        (t4, "What is 'Paging' in memory management systems?",
         "A non-contiguous memory allocation scheme where physical memory is divided into fixed-size frames and logical memory into same-size pages",
         "Writing software documentation in text pages", "Sorting records alphabetically", "Beeping a pager over radio signals", "A", "Easy"),
        (t4, "What is the purpose of the Translation Lookaside Buffer (TLB)?",
         "A high-speed associative hardware cache that stores recent virtual-to-physical page translations to avoid double memory accesses",
         "A swap file on disk", "A temporary register for floating point division", "A network cache for DNS lookups", "A", "Medium"),
        (t4, "What event occurs when a process attempts to access a virtual memory page that is marked as invalid (not currently present in physical RAM)?",
         "General Protection Fault and system reboot", "Page Fault (triggering OS to load the page from disk swap into an available frame)",
         "Segmentation dump and process termination", "Buffer overflow vulnerability", "B", "Easy"),
        (t4, "Which optimal page replacement algorithm has the theoretical lowest page-fault rate on all reference strings (Belady's Optimal)?",
         "Replace the page that will not be used for the longest period of time in the future (OPT / MIN)",
         "Replace the page that was brought into memory earliest (FIFO)",
         "Replace the page that was used least recently (LRU)", "Replace a randomly chosen page", "A", "Medium"),
        (t4, "What counter-intuitive anomaly occurs in First-In, First-Out (FIFO) page replacement where allocating more page frames results in more page faults?",
         "Belady's Anomaly", "Amdahl's Paradox", "Turing Halting Flaw", "Dijkstra Bottleneck", "A", "Easy"),
        (t4, "How does the Least Recently Used (LRU) page replacement algorithm select a victim page?",
         "It replaces the page that has not been referenced for the longest period of past time",
         "It replaces the newest page in memory", "It replaces the page with the highest logical address",
         "It replaces the smallest page", "A", "Easy"),
        (t4, "What is 'Thrashing' in virtual memory systems?",
         "A catastrophic system state where the CPU spends more time paging (swapping pages in and out of disk) than executing actual process instructions",
         "Overheating of the cooling fans", "Deleting temporary files during boot", "Formatting hard drives rapidly", "A", "Medium"),
        (t4, "What model formulated by Peter Denning defines the set of pages that a process is actively referencing during a time window delta?",
         "Working-Set Model", "Buddy Memory Allocation Model", "Two-Phase Commit Model", "Producer-Consumer Model", "A", "Hard")
    ]

    u5 = "Unit 5: File Management and Mass-Storage Structure"
    t5 = "File Systems & Disk Scheduling"
    os_u5 = [
        (t5, "What data structure in UNIX file systems represents a file and stores its metadata (size, permissions, timestamps, block pointers)?",
         "File Allocation Table (FAT)", "Inode (Index Node)", "Superblock only", "Master Boot Record (MBR)", "B", "Easy"),
        (t5, "Which file allocation method suffers from severe external fragmentation and requires knowing file size in advance?",
         "Contiguous Allocation", "Linked Allocation", "Indexed Allocation", "B-Tree Allocation", "A", "Medium"),
        (t5, "In Indexed File Allocation (such as in UNIX inodes), what do 'Indirect Blocks' provide?",
         "Pointers to additional disk blocks containing pointers to data blocks, allowing the file system to support very large files",
         "Encrypted password storage", "Direct backup to cloud storage", "Audio drivers for media playback", "A", "Medium"),
        (t5, "What is the primary role of a Directory in a file system?",
         "To map human-readable file names to their corresponding file descriptors (inumbers / inode references)",
         "To store physical transistor charges", "To speed up internet connectivity", "To format disk tracks", "A", "Easy"),
        (t5, "Which Disk Scheduling algorithm serves I/O requests in the exact order they arrive in the disk request queue?",
         "First-Come, First-Served (FCFS)", "Shortest Seek Time First (SSTF)", "SCAN (Elevator Algorithm)", "C-SCAN (Circular SCAN)", "A", "Easy"),
        (t5, "What is the potential disadvantage of the Shortest Seek Time First (SSTF) disk scheduling algorithm?",
         "It may cause starvation for distant disk cylinder requests if closer requests arrive continuously",
         "It moves the disk arm across the entire disk platter on every request", "It requires flash SSD storage",
         "It cannot handle read requests", "A", "Medium"),
        (t5, "How does the SCAN (Elevator) disk scheduling algorithm move the disk arm?",
         "The arm starts at one end of the disk and moves toward the other end, servicing requests along the way, then reverses direction",
         "The arm jumps randomly to any track", "The arm services the smallest file first", "The arm remains stationary at cylinder 0", "A", "Easy"),
        (t5, "How does C-SCAN (Circular SCAN) differ from the standard SCAN algorithm?",
         "When it reaches the end of the disk, it immediately returns to the beginning without servicing any requests on the return trip, providing more uniform wait times",
         "It never changes direction", "It only scans circular tracks on CDs", "It uses optical lasers instead of magnetic heads", "A", "Medium"),
        (t5, "What three components define the total disk access time for a traditional mechanical Hard Disk Drive (HDD)?",
         "Seek Time + Rotational Latency + Data Transfer Time", "CPU Clock Speed + Bus Width + RAM Size",
         "Baud Rate + Parity Bit + Stop Bit", "Ping Latency + DNS Lookup + TLS Handshake", "A", "Medium"),
        (t5, "What is 'Swap Space' on secondary storage?",
         "Disk space allocated by the OS to temporarily hold inactive memory pages swapped out from physical RAM",
         "A folder for storing downloaded music", "A partition used exclusively for OS installation files", "A hardware buffer inside the keyboard", "A", "Easy"),
        (t5, "What RAID level provides pure data striping across multiple disks without redundancy or parity (yielding maximum performance but zero fault tolerance)?",
         "RAID 0", "RAID 1 (Mirroring)", "RAID 5 (Distributed Parity)", "RAID 6 (Dual Parity)", "A", "Easy"),
        (t5, "What RAID configuration mirrors identical data onto two or more disks to provide high fault tolerance?",
         "RAID 0", "RAID 1", "RAID 5", "RAID 10", "B", "Easy")
    ]

    for q in os_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in os_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in os_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in os_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in os_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_data_analytics_questions():
    questions = []
    sub = "Data Analytics"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester IV"

    u1 = "Unit 1: Statistical Data and Concepts"
    t1 = "Statistical Methods & Sampling"
    da_u1 = [
        (t1, "What type of bias occurs when certain members of the intended population are systematically more likely to be selected in a sample?",
         "Selection / Sampling Bias", "Survivorship Bias", "Omitted Variable Bias", "Publication Bias", "A", "Easy"),
        (t1, "In statistical hypothesis testing, what is a Type I Error (alpha)?",
         "Rejecting the Null Hypothesis (H0) when it is actually true (False Positive)",
         "Failing to reject the Null Hypothesis when it is false (False Negative)",
         "Calculating the standard deviation incorrectly", "Using a non-parametric test on normal data", "A", "Medium"),
        (t1, "What is a Type II Error (beta) in hypothesis testing?",
         "Failing to reject the Null Hypothesis when it is false (False Negative)",
         "Rejecting the Null Hypothesis when it is true (False Positive)",
         "A software syntax error", "Dividing by zero in variance calculation", "A", "Medium"),
        (t1, "What does the 'Statistical Power' of a hypothesis test represent?",
         "1 - beta (the probability of correctly rejecting the null hypothesis when it is false)",
         "The sample size multiplied by the mean", "The p-value threshold", "The alpha significance level", "A", "Hard"),
        (t1, "What does a P-value represent in statistical hypothesis testing?",
         "The probability of observing sample data at least as extreme as the observed data, assuming the null hypothesis is true",
         "The probability that the alternate hypothesis is 100% true",
         "The percentage of missing records in the dataset", "The correlation coefficient between features", "A", "Medium"),
        (t1, "In Exploratory Data Analysis (EDA), which numerical method replaces missing values with computed statistics like mean, median, or mode?",
         "Imputation", "Encoding", "Discretization", "Normalization", "A", "Easy"),
        (t1, "Which outlier detection rule flags observations beyond Q1 - 1.5*IQR and Q3 + 1.5*IQR as statistical outliers?",
         "Tukey's Boxplot / IQR Rule", "Z-score 3-sigma rule", "Cook's Distance", "Mahalanobis rule", "A", "Easy"),
        (t1, "What is a 'Confounding Variable' in statistical modeling?",
         "An unmeasured or unadjusted extraneous variable that influences both the independent variable and the dependent variable, creating a spurious association",
         "A variable with non-numeric values", "A variable with zero variance", "The primary target class", "A", "Medium"),
        (t1, "What is a 95% Confidence Interval for a population mean?",
         "A range of values computed from a sample such that 95% of such intervals constructed from repeated independent samples will contain the true population mean",
         "A guarantee that exactly 95% of individual data values fall within the bounds",
         "A test with 5% sample size", "A non-parametric correlation measure", "A", "Medium"),
        (t1, "What are 'Degrees of Freedom' (df) in calculating sample variance s^2 = sum(x - x_bar)^2 / (n - 1)?",
         "The number of independent values or quantities that can be assigned arbitrarily in a statistical calculation (n - 1 due to fixed sample mean)",
         "The total number of rows in the dataset", "The number of categories in a column", "The range between max and min", "A", "Hard"),
        (t1, "What characterizes Non-Parametric statistical tests compared to Parametric tests?",
         "Non-parametric tests do not assume a specific underlying probability distribution (such as normality) for the population data",
         "Non-parametric tests only accept integer values", "Non-parametric tests cannot compute p-values", "Non-parametric tests are only run on supercomputers", "A", "Medium"),
        (t1, "Which visualization plot in EDA displays bivariate relationships across all feature pairs alongside univariate distributions?",
         "Pairplot / Scatter Plot Matrix", "Pie Chart", "Sankey Diagram", "Treemap", "A", "Easy")
    ]

    u2 = "Unit 2: Descriptive Statistics"
    t2 = "Measures of Central Tendency & Dispersion"
    da_u2 = [
        (t2, "Which measure of central tendency is most robust to extreme outliers in a heavily skewed dataset (such as income distribution)?",
         "Arithmetic Mean", "Median", "Mode", "Midrange", "B", "Easy"),
        (t2, "What is the Mode of the dataset: [4, 7, 2, 7, 9, 7, 5, 2]?",
         "7", "2", "5.375", "4", "A", "Easy"),
        (t2, "What does 'Standard Deviation' measure in descriptive statistics?",
         "The spread or dispersion of data points relative to their arithmetic mean",
         "The middle value of a sorted list", "The difference between maximum and minimum values", "The total count of observations", "A", "Easy"),
        (t2, "What is the relationship between Variance and Standard Deviation?",
         "Standard Deviation is the positive square root of Variance", "Variance is the square root of Standard Deviation",
         "Variance is Standard Deviation divided by sample size N", "There is no mathematical relationship", "A", "Easy"),
        (t2, "What does 'Skewness' measure in a frequency distribution?",
         "The asymmetry or lack of symmetry of a probability distribution around its mean",
         "The peakedness or flatness of the distribution tail", "The sample size", "The number of outliers", "A", "Medium"),
        (t2, "In a positively skewed (right-skewed) distribution, what is the typical relationship among the three central tendency measures?",
         "Mode < Median < Mean", "Mean < Median < Mode", "Mean = Median = Mode", "Median < Mode < Mean", "A", "Medium"),
        (t2, "What does 'Kurtosis' quantify regarding a probability distribution?",
         "The heaviness of tails and peakedness of the distribution relative to a standard normal distribution (mesokurtic)",
         "The direction of the skew", "The correlation between two features", "The number of categorical variables", "A", "Medium"),
        (t2, "A distribution with heavier tails and a sharper peak than the normal distribution (excess kurtosis > 0) is classified as:",
         "Leptokurtic", "Platykurtic", "Mesokurtic", "Uniform", "A", "Medium"),
        (t2, "What is the First Quartile (Q1) of an ordered dataset?",
         "The 25th percentile value below which 25% of the data falls", "The 50th percentile (median)",
         "The average of minimum and maximum", "The 75th percentile", "A", "Easy"),
        (t2, "How is the Interquartile Range (IQR) calculated?",
         "IQR = Q3 - Q1", "IQR = Max - Min", "IQR = Mean - Median", "IQR = Variance / 2", "A", "Easy"),
        (t2, "What is the Coefficient of Variation (CV) used for in comparative statistical analysis?",
         "CV = (Standard Deviation / Mean) * 100%, expressing relative dispersion independent of measurement units",
         "CV = Mean / Variance", "CV = Mode - Median", "CV = Sample size N / 100", "A", "Hard"),
        (t2, "Which summary metric calculates the difference between the 90th percentile and the 10th percentile to measure central dispersion?",
         "Interdecile Range", "Interquartile Range", "Standard Error", "Range", "A", "Hard")
    ]

    u3 = "Unit 3: Data Transformation and Standardization"
    t3 = "Data Normalization & Transforms"
    da_u3 = [
        (t3, "What is the mathematical goal of the Box-Cox Power Transformation?",
         "To transform non-normal, skewed positive continuous data into an approximately normal (Gaussian) distribution",
         "To convert text strings into numerical vectors", "To reduce dataset rows by 50%", "To remove missing values", "A", "Medium"),
        (t3, "What mathematical restriction exists when applying the standard Box-Cox transformation y = (x^lambda - 1) / lambda?",
         "Input values x must be strictly strictly positive (x > 0)", "Input values must be negative integers",
         "Lambda must be equal to 0", "Data must already follow a normal distribution", "A", "Hard"),
        (t3, "Which transformation variant of Box-Cox can handle zero and negative values (Yeo-Johnson)?",
         "Yeo-Johnson Transformation", "Freeman-Tukey Transformation", "Min-Max Scaler", "Logit Transform", "A", "Medium"),
        (t3, "What formula scales a feature x into the bounded range [0, 1] using Min-Max Normalization?",
         "x_scaled = (x - x_min) / (x_max - x_min)", "x_scaled = (x - mean) / std", "x_scaled = log(x)", "x_scaled = x^2", "A", "Easy"),
        (t3, "What formula standardizes a feature x to have zero mean (mu = 0) and unit variance (sigma = 1) via Z-score Standardization?",
         "z = (x - mean) / std", "z = (x - min) / (max - min)", "z = sqrt(x)", "z = exp(x)", "A", "Easy"),
        (t3, "When is standard Log Transformation (y = log(x)) commonly applied to a numerical feature?",
         "When data is heavily right-skewed with long tails spanning several orders of magnitude (e.g. monetary wealth, website traffic)",
         "When data is normally distributed", "When data contains categorical strings", "When data is strictly zero", "A", "Easy"),
        (t3, "What does the 'Logit Transform' compute for a probability or proportion p where 0 < p < 1?",
         "logit(p) = ln(p / (1 - p))", "logit(p) = p^2", "logit(p) = 1 / p", "logit(p) = sqrt(p * (1 - p))", "A", "Medium"),
        (t3, "Why is the Freeman-Tukey transformation (square root and arcsine transform) used on Poisson count or binomial proportion data?",
         "To stabilize the variance of count data across varying mean levels", "To convert integer counts into categorical classes",
         "To invert the matrix", "To double the sample size", "A", "Hard"),
        (t3, "In Min-Max scaling of a feature with range [10, 50], what is the normalized value of an observation x = 30?",
         "0.50", "0.25", "0.75", "0.40", "A", "Easy"),
        (t3, "Why is Z-score standardization preferred over Min-Max scaling when the dataset contains extreme outliers?",
         "Min-Max scaling compresses inliers into a tiny sub-interval because min and max are dictated by outliers; Z-score does not bound data to a fixed interval",
         "Min-Max scaling requires GPU computing", "Z-score deletes outliers automatically", "Z-score converts variables into booleans", "A", "Medium"),
        (t3, "What is 'Robust Scaler' in Scikit-Learn that standardizes features using statistics robust to outliers?",
         "Scales features by subtracting the Median and dividing by the Interquartile Range (IQR)",
         "Scales features by multiplying by pi", "Scales features between -100 and +100", "Uses PCA eigenvalues", "A", "Medium"),
        (t3, "What is 'Discretization / Binning' in data transformation?",
         "Converting continuous numerical variables into discrete categorical intervals or buckets (e.g. Age into Age-Groups)",
         "Deleting columns with high variance", "Calculating the inverse of a covariance matrix", "Sorting arrays with quicksort", "A", "Easy")
    ]

    u4 = "Unit 4: Classical Tests and Contingency Tables"
    t4 = "Hypothesis Tests & Goodness of Fit"
    da_u4 = [
        (t4, "When is a One-Sample Z-Test applied instead of a One-Sample Student's t-Test to test population mean?",
         "When the population standard deviation (sigma) is known and/or the sample size is large (N >= 30) by the Central Limit Theorem",
         "When sample size N is less than 5 and variance is unknown", "When data is purely qualitative and categorical",
         "When comparing more than 5 groups simultaneously", "A", "Medium"),
        (t4, "What distribution does Student's t-distribution approach as the sample size / degrees of freedom N approaches infinity?",
         "Standard Normal Distribution Z ~ N(0, 1)", "Chi-Square Distribution", "Binomial Distribution", "Uniform Distribution", "A", "Easy"),
        (t4, "Which statistical goodness-of-fit test tests whether sample data was drawn from a normally distributed population (widely recognized for high power)?",
         "Shapiro-Wilk Test (or Anderson-Darling)", "Pearson Correlation", "Levene's Test", "Kruskal-Wallis Test", "A", "Medium"),
        (t4, "What does the Kolmogorov-Smirnov (K-S) two-sample test evaluate?",
         "Whether two underlying one-dimensional continuous distributions differ significantly based on the maximum vertical distance between their empirical cumulative distributions",
         "The equality of regression slopes", "The Pearson correlation coefficient", "The ratio of two variances", "A", "Hard"),
        (t4, "What test evaluates whether an observed frequency distribution of categorical counts matches an expected theoretical distribution?",
         "Chi-Square (chi^2) Goodness-of-Fit Test", "Two-sample t-test", "Linear Regression F-test", "Paired t-test", "A", "Easy"),
        (t4, "What is the formula for the Chi-Square statistic across k categories?",
         "chi^2 = sum( (O_i - E_i)^2 / E_i )", "chi^2 = sum( O_i - E_i )", "chi^2 = (Mean - Median) / Std", "chi^2 = O_i / E_i", "A", "Easy"),
        (t4, "When analyzing a 2x2 contingency table with small expected cell frequencies (E < 5), which exact test is preferred over the Chi-Square test?",
         "Fisher's Exact Test", "Two-sample Z-test", "Spearman Rank Test", "Welch's t-test", "A", "Medium"),
        (t4, "What test is used on paired nominal data (before-and-after observations on the same subjects, e.g. treatment response) in a 2x2 table?",
         "McNemar's Test", "Independent two-sample t-test", "ANOVA F-test", "Mann-Whitney U test", "A", "Hard"),
        (t4, "In an independent two-sample t-test, what does Welch's t-test account for that the standard Student's t-test assumes?",
         "Welch's t-test does not assume equal population variances (heteroscedasticity) between the two independent groups",
         "Welch's t-test assumes categorical targets", "Welch's t-test only works for samples of size N=1", "Welch's t-test assumes non-random sampling", "A", "Medium"),
        (t4, "What test is appropriate to test whether the means of two matched/paired groups (e.g. pre-test vs post-test for the same student) differ significantly?",
         "Paired Samples t-Test (Dependent t-test)", "Independent Two-Sample Z-Test", "One-Way ANOVA", "Chi-Square Test of Independence", "A", "Easy"),
        (t4, "In a Chi-Square test of independence on a contingency table with r rows and c columns, what are the degrees of freedom?",
         "df = (r - 1) * (c - 1)", "df = r * c", "df = r + c - 1", "df = n - 1", "A", "Medium"),
        (t4, "What does the Jarque-Bera goodness-of-fit test evaluate to check for normality in sample data?",
         "Whether the sample skewness and excess kurtosis jointly match that of a normal distribution (skewness=0, kurtosis=3)",
         "Whether the mean equals zero", "Whether the median equals the mode", "Whether data has no missing values", "A", "Hard")
    ]

    u5 = "Unit 5: Analysis of Variance and Covariance"
    t5 = "ANOVA & Non-Parametric Variance Tests"
    da_u5 = [
        (t5, "What is the primary statistical purpose of One-Way Analysis of Variance (ANOVA)?",
         "To test whether the means of three or more independent groups are statistically significantly different",
         "To test the correlation between two continuous variables", "To classify images into clusters", "To predict time series trends", "A", "Easy"),
        (t5, "Why is One-Way ANOVA preferred over running multiple pairwise two-sample t-tests across 4 or more groups?",
         "Running multiple pairwise t-tests inflates the Family-Wise Type I Error rate (probability of false positives)",
         "t-tests cannot calculate means", "ANOVA does not require computers", "ANOVA only works for 2 groups", "A", "Medium"),
        (t5, "What test statistic is computed in ANOVA as the ratio of Between-Group Variance to Within-Group Variance (MSB / MSW)?",
         "F-Statistic (Fisher-Snedecor F)", "t-Statistic", "Z-Score", "Chi-Square statistic", "A", "Easy"),
        (t5, "What three core assumptions underlie standard One-Way ANOVA?",
         "Independence of observations, Normality of residuals within groups, and Homogeneity of variances (Homoscedasticity)",
         "Multicollinearity, Zero mean, Infinite degrees of freedom", "Discrete target, Binary features, Non-zero mode",
         "Equidistant quantiles, Zero variance, Logarithmic scale", "A", "Medium"),
        (t5, "Which statistical test is commonly used to test the assumption of Homogeneity of Variances across groups before performing ANOVA?",
         "Levene's Test (or Bartlett's Test)", "Shapiro-Wilk Test", "Durbin-Watson Test", "Kruskal-Wallis Test", "A", "Medium"),
        (t5, "What is the non-parametric alternative to One-Way ANOVA when normality or homoscedasticity assumptions are severely violated?",
         "Kruskal-Wallis H Test (One-Way ANOVA on Ranks)", "Mann-Whitney U Test", "Wilcoxon Signed-Rank Test", "Friedman Test", "A", "Medium"),
        (t5, "What is the non-parametric equivalent of Repeated-Measures ANOVA used to compare three or more paired/matched groups?",
         "Friedman Test", "Kruskal-Wallis Test", "Mood's Median Test", "Chi-Square Test", "A", "Hard"),
        (t5, "What is the non-parametric alternative to the independent two-sample t-test to compare two independent groups?",
         "Wilcoxon Rank-Sum Test / Mann-Whitney U Test", "Paired t-test", "One-Way ANOVA", "Z-Test for proportions", "A", "Easy"),
        (t5, "What does ANCOVA (Analysis of Covariance) do that standard ANOVA cannot?",
         "It includes one or more continuous covariates to statistically control for their confounding effects while comparing group means",
         "It eliminates the need for dependent variables", "It runs faster on GPU clusters", "It computes non-linear decision trees", "A", "Hard"),
        (t5, "What does Two-Way ANOVA allow researchers to test that One-Way ANOVA cannot?",
         "The main effects of two independent categorical factors simultaneously, as well as the Interaction Effect between them",
         "Two different dependent variables in the same model", "The correlation between two rows", "The median of two populations", "A", "Medium"),
        (t5, "What post-hoc test is commonly conducted following a statistically significant ANOVA result to determine which specific pairs of group means differ?",
         "Tukey's Honestly Significant Difference (HSD) Test", "Z-Test", "Normal Equation", "Elbow Test", "A", "Medium"),
        (t5, "What does MANOVA (Multivariate Analysis of Variance) evaluate?",
         "Differences across group means when there are two or more correlated continuous dependent variables evaluated simultaneously",
         "Variance of a single variable across 100 groups", "The accuracy of neural networks", "The bandwidth of cloud servers", "A", "Hard")
    ]

    for q in da_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in da_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in da_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in da_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in da_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_prob_stats_questions():
    questions = []
    sub = "Probability and Statistics"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester IV"

    u1 = "Unit 1: Probability Theory"
    t1 = "Probability Axioms & Bayes Theorem"
    ps_u1 = [
        (t1, "According to Kolmogorov's Axioms of Probability, what is the probability of the entire sample space S, P(S)?",
         "0.0", "1.0", "0.5", "Infinity", "B", "Easy"),
        (t1, "If two events A and B are mutually exclusive (disjoint), what is P(A and B)?",
         "P(A) * P(B)", "0", "1", "P(A) + P(B)", "B", "Easy"),
        (t1, "What is the general Addition Rule of probability for any two non-mutually exclusive events A and B?",
         "P(A or B) = P(A) + P(B) - P(A and B)", "P(A or B) = P(A) * P(B)", "P(A or B) = P(A) / P(B)", "P(A or B) = P(A) + P(B) + P(A and B)", "A", "Easy"),
        (t1, "If events A and B are statistically independent, what does P(A and B) equal?",
         "P(A) + P(B)", "P(A) * P(B)", "P(A | B)", "0", "B", "Easy"),
        (t1, "What is the formula for the Conditional Probability of event A given that event B has occurred, P(A | B)?",
         "P(A | B) = P(A and B) / P(B) (provided P(B) > 0)", "P(A | B) = P(A) * P(B)", "P(A | B) = P(A) + P(B)", "P(A | B) = P(B) / P(A)", "A", "Easy"),
        (t1, "What fundamental theorem calculates the posterior probability of a cause given observed evidence: P(A_i | B)?",
         "Central Limit Theorem", "Bayes' Theorem of Inverse Probability", "Markov's Inequality", "Chebyshev's Inequality", "B", "Easy"),
        (t1, "In Bayes' theorem, what is P(A) known as before observing new evidence B?",
         "Posterior Probability", "Prior Probability", "Likelihood", "Evidence", "B", "Easy"),
        (t1, "A fair 6-sided die is rolled. What is the probability of obtaining an even number or a number greater than 4?",
         "2/3", "1/2", "5/6", "1/3", "A", "Medium"),
        (t1, "Two cards are drawn sequentially without replacement from a standard 52-card deck. What is the probability that both cards are Aces?",
         "(4/52) * (3/51) = 1/221", "(4/52) * (4/52)", "(1/52) * (1/51)", "4/52", "A", "Medium"),
        (t1, "What is the Total Probability Rule used in the denominator of Bayes' theorem?",
         "P(B) = sum_{i=1}^n P(A_i) * P(B | A_i) for a partition {A_1, ..., A_n}", "P(B) = prod_{i=1}^n P(A_i)", "P(B) = 1 - P(A)", "P(B) = max(P(A_i))", "A", "Hard"),
        (t1, "If P(A) = 0.4, P(B) = 0.5, and A and B are independent, what is P(A or B)?",
         "0.70", "0.90", "0.20", "0.50", "A", "Medium"),
        (t1, "What is the empirical (relative frequency) definition of probability as the number of experimental trials N approaches infinity?",
         "The limit of the relative frequency of occurrence of the event as N -> infinity", "A subjective belief rating",
         "The ratio of favorable cases to total possible cases in a finite space", "The square root of sample variance", "A", "Easy")
    ]

    u2 = "Unit 2: Random Variable and Mathematical Expectation"
    t2 = "Random Variables, PMF, PDF & Expectation"
    ps_u2 = [
        (t2, "What is the fundamental difference between a Discrete Random Variable and a Continuous Random Variable?",
         "A discrete random variable takes on countable values; a continuous random variable takes on any value within an uncountable real interval",
         "Discrete variables cannot be negative", "Continuous variables can only take integers", "There is no difference in probability theory", "A", "Easy"),
        (t2, "For a continuous random variable X with Probability Density Function f(x), what is the total area under the curve from -infinity to +infinity?",
         "0.0", "1.0", "pi", "Infinity", "B", "Easy"),
        (t2, "For any discrete random variable X, what is the mathematical definition of its Expected Value E[X]?",
         "E[X] = sum_{x} x * P(X = x)", "E[X] = sum_{x} P(X = x)", "E[X] = max(x)", "E[X] = (max - min) / 2", "A", "Easy"),
        (t2, "How is the Variance of a random variable X mathematically expressed in terms of expectations?",
         "Var(X) = E[X^2] - (E[X])^2", "Var(X) = E[X] - E[X^2]", "Var(X) = (E[X])^2", "Var(X) = sqrt(E[X])", "A", "Easy"),
        (t2, "If a and b are constants and X is a random variable, what is the expected value of the linear combination E[a*X + b]?",
         "a * E[X] + b", "a^2 * E[X] + b", "E[X] + a * b", "a * E[X]", "A", "Easy"),
        (t2, "What is the variance of a constant c, Var(c)?",
         "c", "0", "1", "c^2", "B", "Easy"),
        (t2, "For any two independent random variables X and Y, what does the Covariance Cov(X, Y) equal?",
         "0", "1", "Var(X) * Var(Y)", "E[X] * E[Y]", "A", "Medium"),
        (t2, "If X and Y are independent random variables, what does Var(X - Y) equal?",
         "Var(X) + Var(Y)", "Var(X) - Var(Y)", "Var(X) * Var(Y)", "0", "A", "Medium"),
        (t2, "What function F(x) = P(X <= x) gives the cumulative probability that a random variable X takes a value less than or equal to x?",
         "Cumulative Distribution Function (CDF)", "Probability Mass Function (PMF)", "Moment Generating Function (MGF)", "Characteristic Function", "A", "Easy"),
        (t2, "For a continuous random variable X, what is the probability of X taking on an exact single point value, P(X = c)?",
         "1.0", "0.0", "f(c)", "0.5", "B", "Medium"),
        (t2, "What does the Marginal Probability Mass Function P(X = x) represent in a joint distribution of (X, Y)?",
         "P(X = x) = sum_{y} P(X = x, Y = y)", "P(X = x) = P(X = x, Y = y) / P(Y = y)", "P(X = x) = max_y P(X, Y)", "P(X = x) = 1", "A", "Hard"),
        (t2, "What is the mathematical expectation E[X] for the outcome of rolling a fair 6-sided die?",
         "3.5", "3.0", "4.0", "2.5", "A", "Easy")
    ]

    u3 = "Unit 3: Theoretical Probability Distributions"
    t3 = "Binomial, Poisson & Normal Distributions"
    ps_u3 = [
        (t3, "What are the parameters of a Binomial Distribution B(n, p)?",
         "n (number of independent trials) and p (probability of success on each trial)",
         "mu (mean) and sigma (standard deviation)", "lambda (average rate of events)", "a and b (endpoints)", "A", "Easy"),
        (t3, "What is the Mean and Variance of a Binomial Distribution B(n, p)?",
         "Mean = n * p, Variance = n * p * (1 - p)", "Mean = n / p, Variance = n * p^2", "Mean = p, Variance = p * (1 - p)", "Mean = n, Variance = sqrt(n)", "A", "Easy"),
        (t3, "Under what limiting conditions does the Binomial distribution converge to the Poisson distribution?",
         "When n -> infinity, p -> 0, such that lambda = n * p remains a finite constant", "When p = 0.5 and n is small",
         "When n = 1", "When variance is greater than the mean", "A", "Medium"),
        (t3, "What unique mathematical property holds for the Poisson Distribution regarding its mean and variance?",
         "Mean = Variance = lambda", "Mean > Variance", "Variance = Mean^2", "Variance is always 1", "A", "Easy"),
        (t3, "In a Poisson process with an average rate of lambda = 3 occurrences per hour, what is the probability of exactly 0 occurrences in one hour?",
         "e^(-3) approx 0.0498", "0", "3 * e^(-3)", "1 - e^(-3)", "A", "Medium"),
        (t3, "What is the shape of the Probability Density Function curve for a Normal (Gaussian) distribution?",
         "Symmetric, bell-shaped curve centered at the mean mu", "U-shaped curve", "Right-skewed exponential tail", "Flat rectangular box", "A", "Easy"),
        (t3, "What are the parameters that uniquely define a Normal Distribution N(mu, sigma^2)?",
         "Mean (mu) and Variance (sigma^2)", "Degrees of freedom and scale", "Number of successes and trials", "Shape and rate", "A", "Easy"),
        (t3, "What are the Mean and Standard Deviation of the Standard Normal Distribution Z?",
         "Mean = 0, Standard Deviation = 1", "Mean = 1, Standard Deviation = 0", "Mean = 0, Variance = 0", "Mean = 100, Standard Deviation = 15", "A", "Easy"),
        (t3, "According to the Empirical Rule (68-95-99.7 Rule) for a Normal distribution, what percentage of values lie within 2 standard deviations of the mean (mu +- 2*sigma)?",
         "Approximately 95.45%", "Approximately 68.27%", "Approximately 99.73%", "50.0%", "A", "Easy"),
        (t3, "What transformation formula converts any normal random variable X ~ N(mu, sigma^2) into standard normal variable Z ~ N(0, 1)?",
         "Z = (X - mu) / sigma", "Z = (X - sigma) / mu", "Z = X * sigma + mu", "Z = (X - mu)^2 / sigma", "A", "Easy"),
        (t3, "Why is the Normal Distribution of paramount importance in engineering and statistics (Central Limit Theorem)?",
         "The sum (or average) of a large number of independent random variables tends toward a normal distribution regardless of their original distributions",
         "Because it eliminates the need for calculating variances", "Because all data in computers is automatically normal",
         "Because its integral can be solved in basic polynomials", "A", "Medium"),
        (t3, "What is the skewness and kurtosis of a perfect standard normal distribution?",
         "Skewness = 0, Kurtosis = 3 (Excess Kurtosis = 0)", "Skewness = 1, Kurtosis = 1", "Skewness = -1, Kurtosis = 0", "Skewness = 0, Kurtosis = 0", "A", "Hard")
    ]

    u4 = "Unit 4: Correlation"
    t4 = "Correlation Coefficients & Probable Error"
    ps_u4 = [
        (t4, "What does Karl Pearson's correlation coefficient (r) measure between two numerical variables X and Y?",
         "The strength and direction of the linear relationship between X and Y", "The non-linear parabolic dependency",
         "The causal relationship between X and Y", "The difference between their arithmetic means", "A", "Easy"),
        (t4, "What is the mathematically bounded range of Karl Pearson's correlation coefficient r?",
         "-1 <= r <= +1", "0 <= r <= 1", "-infinity < r < +infinity", "0 <= r <= 100", "A", "Easy"),
        (t4, "What does a correlation coefficient of r = -1 indicate?",
         "A perfect negative (inverse) linear relationship where as X increases, Y decreases strictly proportionally",
         "Zero linear relationship", "A perfect positive relationship", "A calculation error", "A", "Easy"),
        (t4, "What does a correlation coefficient of r = 0 between two variables imply?",
         "There is no linear association between the two variables (though a strong non-linear relationship might still exist)",
         "The variables are identical", "The variables have zero variance", "The data points form a perfect circle", "A", "Medium"),
        (t4, "Does correlation imply causation in scientific and engineering data analysis?",
         "No, correlation only measures statistical co-variation, not direct cause-and-effect mechanisms",
         "Yes, correlation always proves causation", "Only when r > 0.95", "Only in medical trials", "A", "Easy"),
        (t4, "Which correlation coefficient is non-parametric and evaluates monotonic relationships based on the ranks of observations?",
         "Spearman's Rank Correlation Coefficient (rho)", "Karl Pearson's r", "Multiple Correlation R", "Auto-regressive coefficient", "A", "Easy"),
        (t4, "What is the formula for Spearman's Rank Correlation Coefficient when there are no tied ranks?",
         "rho = 1 - (6 * sum(d_i^2)) / (n * (n^2 - 1))", "rho = sum(d_i) / n", "rho = (n - 1) / (n + 1)", "rho = 1 / (1 + sum(d_i^2))", "A", "Hard"),
        (t4, "What is the Probable Error (P.E.) of Karl Pearson's correlation coefficient r for a sample of size n?",
         "P.E. = 0.6745 * (1 - r^2) / sqrt(n)", "P.E. = (1 - r) / n", "P.E. = r / sqrt(n - 2)", "P.E. = sqrt(1 - r^2)", "A", "Hard"),
        (t4, "According to statistical rule of thumb, when is a sample correlation coefficient r considered distinctly significant using Probable Error?",
         "When r > 6 * P.E.", "When r < P.E.", "When r = P.E. / 2", "When P.E. = 0", "A", "Hard"),
        (t4, "Is Karl Pearson's correlation coefficient r affected by a change of origin and scale (i.e. u = (x - a)/h, v = (y - b)/k where h, k > 0)?",
         "No, correlation coefficient r is completely invariant to changes of origin and positive changes of scale",
         "Yes, r is multiplied by h * k", "Yes, r becomes zero", "Only change of origin affects r", "A", "Medium"),
        (t4, "What is the geometric interpretation of Pearson's r between two centered zero-mean vectors in linear algebra?",
         "The cosine of the angle theta between the two vectors", "The cross-product magnitude",
         "The Euclidean distance between their endpoints", "The determinant of the 2x2 matrix", "A", "Hard"),
        (t4, "If the correlation coefficient between height and weight is +0.82, what percentage of variation in weight is shared linearly with height (R^2)?",
         "(0.82)^2 approx 67.24%", "82.0%", "41.0%", "18.0%", "A", "Medium")
    ]

    u5 = "Unit 5: Linear Regression Analysis"
    t5 = "Regression Lines & Properties"
    ps_u5 = [
        (t5, "What is the line of regression of Y on X used for?",
         "To estimate or predict the most probable value of dependent variable Y for a given known value of independent variable X",
         "To calculate the mode of X", "To test if data is normally distributed", "To sort the data points", "A", "Easy"),
        (t5, "What is the equation of the regression line of Y on X with means (x_bar, y_bar) and regression coefficient b_yx?",
         "y - y_bar = b_yx * (x - x_bar)", "y = b_yx * x", "x - x_bar = b_xy * (y - y_bar)", "y - y_bar = (x - x_bar) / b_yx", "A", "Easy"),
        (t5, "How is the regression coefficient of Y on X (b_yx) expressed in terms of Pearson's r and standard deviations (sigma_x, sigma_y)?",
         "b_yx = r * (sigma_y / sigma_x)", "b_yx = r * (sigma_x / sigma_y)", "b_yx = sigma_y / (r * sigma_x)", "b_yx = r^2 * (sigma_y / sigma_x)", "A", "Medium"),
        (t5, "What is the fundamental mathematical relationship between correlation coefficient r and the two regression coefficients (b_yx and b_xy)?",
         "r = +- sqrt(b_yx * b_xy)", "r = (b_yx + b_xy) / 2", "r = b_yx / b_xy", "r = b_yx * b_xy", "A", "Medium"),
        (t5, "If both regression coefficients b_yx and b_xy are negative, what must the sign of correlation coefficient r be?",
         "Strictly negative", "Strictly positive", "Zero", "Can be either positive or negative", "A", "Easy"),
        (t5, "What point in the Cartesian coordinate plane do both regression lines (Y on X and X on Y) always intersect at?",
         "The mean point (x_bar, y_bar)", "The origin (0, 0)", "The point of maximum values (x_max, y_max)", "The median point", "A", "Easy"),
        (t5, "If the two regression lines are perpendicular to each other (theta = 90 degrees), what is the value of correlation coefficient r?",
         "r = 0 (no linear correlation)", "r = +1", "r = -1", "r = 0.5", "A", "Medium"),
        (t5, "If the two regression lines coincide with each other (theta = 0 degrees), what does it indicate about the correlation?",
         "There is perfect linear correlation: r = +1 or r = -1", "There is zero correlation", "The regression coefficients are negative", "The data has infinite variance", "A", "Medium"),
        (t5, "Can both regression coefficients b_yx and b_xy be numerically greater than 1 simultaneously?",
         "No, because r^2 = b_yx * b_xy <= 1; if one is greater than 1, the other must be less than 1",
         "Yes, always", "Only if the correlation is positive", "Only if sample size is greater than 100", "A", "Hard"),
        (t5, "What does the Coefficient of Determination (R^2) represent in linear regression?",
         "The proportion of the total variance in the dependent variable that is explained by the regression model",
         "The slope of the regression line", "The p-value of the intercept", "The sample size divided by 2", "A", "Medium"),
        (t5, "What mathematical criterion does Ordinary Least Squares (OLS) use to fit the best regression line?",
         "Minimizing the sum of squared vertical residuals (errors) sum(y_i - y_hat_i)^2",
         "Maximizing the sum of residuals", "Minimizing the number of data points", "Setting the slope to 1", "A", "Easy"),
        (t5, "What is the arithmetic mean of the residuals in an Ordinary Least Squares regression model with an intercept?",
         "Exactly 0", "1.0", "Equal to the variance", "Dependent on the scale of X", "A", "Hard")
    ]

    for q in ps_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ps_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ps_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ps_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ps_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_full_stack_questions():
    questions = []
    sub = "Full Stack Development"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester IV"

    u1 = "Unit 1: Bootstrap and Responsive Layouts"
    t1 = "Bootstrap Grids & Components"
    fs_u1 = [
        (t1, "How many columns does the default Bootstrap grid system contain across a single horizontal row?",
         "12 columns", "10 columns", "16 columns", "8 columns", "A", "Easy"),
        (t1, "Which CSS class in Bootstrap provides a responsive fixed-width container that adapts to breakpoints?",
         "container", "container-fluid", "row", "col", "A", "Easy"),
        (t1, "Which Bootstrap breakpoint corresponds to medium devices like tablets (viewports >= 768px)?",
         "col-md-*", "col-sm-*", "col-lg-*", "col-xl-*", "A", "Easy"),
        (t1, "Which Bootstrap 5 utility class sets text color to blue (theme primary)?",
         "text-primary", "color-blue", "font-primary", "text-main", "A", "Easy"),
        (t1, "How do you make an image responsive in Bootstrap 5 so that it scales with its parent element?",
         "class=\"img-fluid\"", "class=\"img-responsive\"", "class=\"responsive-image\"", "class=\"img-scale\"", "A", "Easy"),
        (t1, "Which class creates a collapsible navigation bar component in Bootstrap?",
         "navbar and navbar-expand-*", "nav-menu-collapse", "header-nav", "nav-accordion", "A", "Easy"),
        (t1, "What Bootstrap class is used on form inputs (<input>, <textarea>) to apply full-width, rounded borders, and focus styling?",
         "form-control", "form-input", "input-modern", "form-group", "A", "Easy"),
        (t1, "Which Bootstrap class adds margin-bottom of size 3 (spacer 1rem)?",
         "mb-3", "bottom-margin-3", "m-b-3", "pad-b-3", "A", "Easy"),
        (t1, "What class creates a card container in Bootstrap 5 with border and padding utilities?",
         "card", "panel", "box-container", "tile", "A", "Easy"),
        (t1, "How does Bootstrap's mobile-first responsive design philosophy work?",
         "Base styles target mobile viewports first, and min-width media queries progressively enhance layouts for larger screens",
         "It only renders on smartphones", "It disables CSS on desktops", "It uses separate HTML files for desktop and mobile", "A", "Medium"),
        (t1, "Which Bootstrap 5 component presents a dialog box / popup window overlaid on top of the current webpage?",
         "Modal", "Alert", "Popover", "Toast", "A", "Easy"),
        (t1, "Which display flex utility in Bootstrap centers child items both horizontally and vertically inside a container?",
         "d-flex justify-content-center align-items-center", "d-center", "flex-center-all", "d-flex float-center", "A", "Easy")
    ]

    u2 = "Unit 2: JavaScript Fundamentals and DOM"
    t2 = "JavaScript Language & DOM Manipulation"
    fs_u2 = [
        (t2, "What is the key difference between 'let' and 'var' in modern ECMAScript (ES6)?",
         "'let' has block scope; 'var' has function scope and undergoes variable hoisting with undefined initialization",
         "'var' cannot be reassigned", "'let' is globally scoped only", "'let' only stores numbers", "A", "Easy"),
        (t2, "What does the 'const' keyword declare in JavaScript?",
         "A block-scoped variable whose identifier reference cannot be reassigned",
         "A variable that must be an integer", "A function that executes continuously", "A global DOM node", "A", "Easy"),
        (t2, "What is 'Hoisting' in JavaScript?",
         "The JavaScript engine's behavior of moving declarations to the top of their containing scope prior to code execution",
         "Uploading code to a remote server", "Converting strings to numbers", "Compressing JavaScript files", "A", "Medium"),
        (t2, "What is the output of the JavaScript expression: typeof null?",
         "\"object\"", "\"null\"", "\"undefined\"", "\"number\"", "A", "Medium"),
        (t2, "What is the difference between the '==' (loose equality) and '===' (strict equality) operators in JavaScript?",
         "'==' performs implicit type coercion before comparison; '===' compares both value and type without coercion",
         "'===' is for objects only", "'==' is an assignment operator", "There is no difference in ES6", "A", "Easy"),
        (t2, "Which DOM method selects the first element matching a specified CSS selector in the document?",
         "document.querySelector()", "document.getElementById()", "document.getElementsByClassName()", "document.findFirst()", "A", "Easy"),
        (t2, "How do you attach a click event handler to a button element in modern JavaScript?",
         "button.addEventListener('click', function(event) { ... })", "button.attachClick(function() { ... })",
         "button.onClickEvent = true", "button.listen('click')", "A", "Easy"),
        (t2, "What is 'Event Bubbling' in the browser DOM event dispatch mechanism?",
         "An event triggers on the innermost target element and then propagates upward through its ancestors in the DOM tree",
         "Events exploding and crashing the page", "Creating visual bubbles on the canvas", "Sending events over WebSockets", "A", "Medium"),
        (t2, "How do you prevent the default action of a form submit event (page reload) in JavaScript?",
         "event.preventDefault()", "event.stopPropagation()", "return false;", "event.halt()", "A", "Easy"),
        (t2, "What method converts a JavaScript object into a JSON formatted string?",
         "JSON.stringify()", "JSON.parse()", "Object.toJSON()", "String.fromObject()", "A", "Easy"),
        (t2, "What does the JavaScript Array.prototype.map() method return?",
         "A new array containing the results of calling a provided function on every element in the calling array",
         "The filtered original array in-place", "A single accumulated primitive value", "A boolean flag", "A", "Easy"),
        (t2, "What is a 'Closure' in JavaScript?",
         "A function bundled together with references to its surrounding lexical state (lexical environment)",
         "Closing a browser tab", "The final line of a script", "A syntax error that halts execution", "A", "Hard")
    ]

    u3 = "Unit 3: jQuery Events and AJAX"
    t3 = "jQuery Library & Asynchronous AJAX"
    fs_u3 = [
        (t3, "What is the primary shorthand symbol used in jQuery to select DOM elements and initialize jQuery operations?",
         "$", "@", "#", "&", "A", "Easy"),
        (t3, "How do you execute jQuery code only after the DOM has fully loaded and is safe to manipulate?",
         "$(document).ready(function() { ... });", "$('window').onLoad(function() { ... });",
         "$.domLoaded(function() { ... });", "$(init);", "A", "Easy"),
        (t3, "Which jQuery method hides selected HTML elements with a smooth sliding up motion?",
         "slideUp()", "fadeOut()", "hideSlow()", "collapse()", "A", "Easy"),
        (t3, "How do you change the CSS background-color of an element with ID 'header' using jQuery?",
         "$('#header').css('background-color', 'blue');", "$('.header').style('blue');",
         "document.css('#header', 'blue');", "$('#header').background('blue');", "A", "Easy"),
        (t3, "What does AJAX stand for in web application development?",
         "Asynchronous JavaScript and XML", "Advanced Java and XHTML", "Automated JavaScript Array Extension", "Application JSON Access XML", "A", "Easy"),
        (t3, "What is the primary user experience advantage of using AJAX in web applications?",
         "Webpages can exchange data with the server asynchronously in the background and update parts of the DOM without reloading the entire page",
         "It makes HTML files smaller on disk", "It eliminates the need for database storage", "It compiles JavaScript to C++", "A", "Easy"),
        (t3, "Which jQuery method is a high-level shorthand for sending an HTTP GET request to a server?",
         "$.get(url, data, successCallback)", "$.fetchGet()", "$.request()", "$.http()", "A", "Easy"),
        (t3, "In a jQuery $.ajax() configuration object, what property specifies the HTTP request method ('GET', 'POST', 'PUT', 'DELETE')?",
         "type (or method)", "action", "protocol", "verb", "A", "Easy"),
        (t3, "What jQuery method iterates over a JavaScript array or object collection?",
         "$.each(collection, callback)", "$.loop()", "$.mapArray()", "$.traverse()", "A", "Easy"),
        (t3, "What modern browser API has largely superseded jQuery AJAX in vanilla modern JavaScript?",
         "Fetch API (fetch())", "XMLHttpRequest v1", "Gopher API", "Socket.IO", "A", "Easy"),
        (t3, "Which jQuery traversal method selects all direct child elements of matched elements?",
         "children()", "parents()", "siblings()", "find()", "A", "Easy"),
        (t3, "What does the jQuery serialize() method do when called on a form element?",
         "Encodes a set of form input elements as a string of name-value pairs suitable for submission in an HTTP request",
         "Converts form data into a PDF", "Encrypts inputs with AES-256", "Deletes form inputs", "A", "Medium")
    ]

    u4 = "Unit 4: PHP and MySQL Integration"
    t4 = "Server-Side PHP & Database Operations"
    fs_u4 = [
        (t4, "What open/close tags enclose server-side PHP scripts inside an HTML document?",
         "<?php ... ?>", "<% ... %>", "<script php> ... </script>", "<!-- php ... -->", "A", "Easy"),
        (t4, "How are variable identifiers declared in PHP syntax?",
         "Starting with a dollar sign: $variableName", "var variableName", "let variableName", "val variableName", "A", "Easy"),
        (t4, "Which PHP superglobal array retrieves form data sent via an HTTP POST request?",
         "$_POST", "$_GET", "$_REQUEST", "$_SERVER", "A", "Easy"),
        (t4, "Which operator is used to concatenate strings in PHP?",
         ". (period / dot operator)", "+ (plus operator)", "& (ampersand)", "~ (tilde)", "A", "Easy"),
        (t4, "What is the difference between single quotes ('') and double quotes (\"\") when declaring strings in PHP?",
         "Double quotes parse variable interpolation and escape sequences; single quotes treat text as literal strings",
         "Single quotes can span multiple lines; double quotes cannot", "Double quotes are deprecated in PHP 8", "There is no difference", "A", "Easy"),
        (t4, "What database extension in modern PHP provides an object-oriented data-access abstraction layer with prepared statement support?",
         "PHP Data Objects (PDO)", "mysql_* extension (deprecated in PHP 7)", "SQLite ODBC exclusively", "Direct socket connections", "A", "Medium"),
        (t4, "Why are prepared statements in PDO (or MySQLi) essential when executing user-input SQL queries?",
         "They completely prevent SQL Injection attacks by parameterizing inputs and separating SQL code from data",
         "They compress the database table on disk", "They execute without a network connection", "They automatically translate SQL into PHP", "A", "Easy"),
        (t4, "Which function in PHP starts a new user session or resumes an existing session using cookie session IDs?",
         "session_start()", "start_session()", "init_session()", "session_begin()", "A", "Easy"),
        (t4, "What superglobal array in PHP stores session variables available across multiple webpage requests?",
         "$_SESSION", "$_COOKIES", "$_GLOBAL", "$_USER", "A", "Easy"),
        (t4, "Which SQL clause is used in a SELECT statement to retrieve only unique records and filter out duplicates?",
         "DISTINCT", "UNIQUE", "GROUP BY only", "FILTER", "A", "Easy"),
        (t4, "What is the primary role of a Foreign Key constraint in a MySQL relational table?",
         "To enforce referential integrity between matching columns in two related tables",
         "To speed up integer arithmetic", "To encrypt user passwords", "To auto-increment row IDs", "A", "Easy"),
        (t4, "Which PHP function encodes an associative array into a valid JSON string to return from a REST API endpoint?",
         "json_encode()", "json_decode()", "array_to_json()", "serialize_json()", "A", "Easy")
    ]

    u5 = "Unit 5: MVC with Laravel Framework"
    t5 = "MVC Pattern & Laravel Architecture"
    fs_u5 = [
        (t5, "What software design pattern separates an application into Model, View, and Controller layers?",
         "Model-View-Controller (MVC) Pattern", "Factory Method Pattern", "Observer Pattern", "Singleton Pattern", "A", "Easy"),
        (t5, "In the MVC architecture, what is the role of the 'Model'?",
         "Managing application data logic, database interactions, business rules, and entity relationships",
         "Rendering HTML and CSS templates for the user interface", "Routing HTTP requests from the browser", "Configuring web server ports", "A", "Easy"),
        (t5, "What command-line interface tool is included with Laravel to generate boilerplate code, run migrations, and start local servers?",
         "Artisan CLI", "Composer CLI", "npm CLI", "Laravel Shell", "A", "Easy"),
        (t5, "What package dependency manager for PHP is required to install Laravel and its third-party library packages?",
         "Composer", "pip", "npm", "Maven", "A", "Easy"),
        (t5, "Where are standard web routes registered and mapped to controller actions in a Laravel project?",
         "routes/web.php", "config/app.php", "app/Models/Route.php", "public/index.php", "A", "Easy"),
        (t5, "What is the powerful, lightweight templating engine provided natively by the Laravel framework?",
         "Blade Templating Engine", "Twig", "Smarty", "Jinja2", "A", "Easy"),
        (t5, "In a Laravel Blade template, what directive is used to inherit a parent layout structure?",
         "@extends('layouts.app')", "@include('layouts.app')", "@import('layouts.app')", "@parent('layouts.app')", "A", "Easy"),
        (t5, "What is 'Eloquent ORM' in the Laravel framework?",
         "An Active Record implementation that provides an intuitive, fluent object-oriented interface for database querying and CRUD operations",
         "A graphical UI editor for HTML", "A hardware caching device", "A web server daemon replacing Apache", "A", "Easy"),
        (t5, "What are 'Database Migrations' in Laravel?",
         "Version control for your database, allowing teams to define, modify, and share the application database schema programmatically",
         "Physically copying SQL data between hard drives", "Exporting database tables into Microsoft Word", "Backing up data to magnetic tape", "A", "Medium"),
        (t5, "What security directive must be included inside all HTML forms submitting POST requests in Laravel to prevent CSRF attacks?",
         "@csrf", "@secure", "@auth", "@token", "A", "Easy"),
        (t5, "Which Artisan command applies all outstanding database migration scripts in Laravel?",
         "php artisan migrate", "php artisan db:run", "php artisan schema:update", "php artisan tables:create", "A", "Easy"),
        (t5, "What Eloquent relationship method defines a One-to-Many relationship on a Model (e.g. a Post has many Comments)?",
         "hasMany(Comment::class)", "belongsTo(Comment::class)", "hasOne(Comment::class)", "belongsToMany(Comment::class)", "A", "Easy")
    ]

    for q in fs_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in fs_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in fs_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in fs_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in fs_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_all_sem4_questions():
    all_q = []
    all_q.extend(get_os_questions())
    all_q.extend(get_data_analytics_questions())
    all_q.extend(get_prob_stats_questions())
    all_q.extend(get_full_stack_questions())
    return all_q
