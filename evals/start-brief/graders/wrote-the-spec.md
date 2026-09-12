---
type: tool_used
tool: Write
input_match: "project_spec\\.md"
---
The spec was rewritten by the run, not left as the example. (A leading `/start` in the prompt is expanded by the harness without a Skill tool call, so `tool_used: Skill` cannot serve as the plugin-fired indicator here — measured on the first real run.)
