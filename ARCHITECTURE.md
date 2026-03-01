# Windows on Linux System Architecture

```plaintext
                      +---------------+
                      |  Runner Script |
                      +-------+-------+
                              |
                              v
                      +---------------+
                      |     Proton    |
                      +-------+-------+
                              |
                              v
                      +---------------+
                      |      Wine     |
                      +---------------+
                              |
                      +---------------+
                      |   Windows App  |
                      +---------------+
```

## Detailed Explanation

- **Runner Script**: This script serves as the entry point for executing Windows applications on Linux. It initializes the environment and calls Proton.

- **Proton**: A compatibility layer built on top of Wine and specifically optimized for running Windows games. It manages the settings and configurations needed for the Windows applications.

- **Wine**: A software that allows Windows applications to run on Linux by providing the necessary Windows API calls.

- **Windows App**: The actual application being executed. The runner script passes it through Proton, which then utilizes Wine to run the application seamlessly on Linux.
