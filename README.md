# Claude Code Native Hooks Integration

## Overview

This project provides an initial Python implementation for collecting and logging events from Claude Code using its native hooks to explore the information available through them, including user prompts, tool calls, execution results, and session activities.



## Implementation

* The implementation consists of two main classes:

  1. **HookReceiver**: Reads JSON event data from Claude Code through standard input (stdin), checks that the received data is a JSON object, and raises an error when the JSON is invalid.
  2. **EventLogger**: Copies the received event without removing its original fields, adds a UTC timestamp (captured\_at), and saves the event data to a local JSONL file (ClaudeEvents.jsonl).



* The .claude/settings.json file registers command hooks for the selected events, where each hook is configured to execute the same Python script, hook\_handler.py, with a timeout of 10 seconds. No matchers are currently specified.





## Supported Hook Events

The current configuration registers the following 12 events:



|Category|Hook Event|When it fires|
|-|-|-|
|Prompt submissions|UserPromptSubmit|When a prompt is submitted, before Claude processes it|
|Tool calls|PreToolUse|Before a tool call executes.|
|Execution results|PostToolUse|After a tool call succeeds.|
|Execution failures|PostToolUseFailure|After a tool call fails|
|Permissions|PermissionRequest|When a tool call needs a permission decision|
|Permissions|PermissionDenied|When auto mode denies a tool call, including denials without a classifier verdict.|
|Session lifecycle|SessionStart|When a session begins or resumes|
|Session lifecycle|SessionEnd|When a session terminates|
|Agent activity|Stop|When Claude finishes responding|
|Agent activity|StopFailure|When the turn ends due to an API error|
|Subagent activity|SubagentStart|When a subagent is spawned|
|Subagent activity|SubagentStop|When a subagent finishes|





## Testing

The Python logger was tested locally using a sample JSON event passed through standard input:

* test\_event.json contains the sample input event.
* ClaudeEvents.jsonl contains the logged output, including the captured\_at timestamp.



The configuration file was also checked for valid JSON syntax.





## Limitations

* The log file currently uses a relative path, so its location depends on the working directory of the process.
* The logger records only events exposed through the configured native hooks.
* The logger stores the complete event payload without filtering sensitive information.
* The current implementation stores events locally without filtering or masking sensitive data.
* Compatibility with different Claude Code environments and versions has not been tested.



### Note: 

The current hook configuration does not explicitly include `"onFailure": "continue"`, which could be added to allow Claude Code to continue execution if a hook fails or times out.

