### Claude Code Native Hooks Integration

##### Overview

This project provides an initial Python implementation for collecting and logging events from Claude Code using its native hooks to explore the information available through them, including user prompts, tool calls, execution results, and session activities.


##### Implementation

The implementation consists of two main classes:

* **HookReceiver**: Reads JSON event data from standard input (stdin) and validates its structure.
* **EventLogger**: Adds a UTC timestamp (captured\_at) and saves the event data to a local JSONL file (ClaudeEvents.jsonl).

The logger preserves all fields received from Claude Code without requiring separate handlers for each event type.


##### Testing

The Python logger was tested locally using a sample JSON event passed through standard input.

* test\_event.json contains the sample input event.
* ClaudeEvents.jsonl contains the logged output, including the captured\_at timestamp.


##### Limitations

* Native hooks expose specific events, not all internal agent activities or reasoning.
* Available fields vary depending on the hook event.
* Logs may contain sensitive information and should not be committed to GitHub.
* The current implementation stores events locally without filtering or masking sensitive data.

