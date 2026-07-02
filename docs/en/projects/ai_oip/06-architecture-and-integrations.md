# Architecture and Integrations

## Architecture

## Tool Gateway pattern

All data access goes through controlled HTTP tools with explicit input contracts, validation, structured output, and metadata.

## Playbook-based diagnostics

The system routes questions to domain-specific diagnostic playbooks instead of exposing all tools to the LLM at once.

Each business domain exposes a bounded set of allowed tools, diagnostic steps, constraints, and expected evidence.

## Tool Registry

Implemented and evolved the Tool Registry concept as a machine-readable catalog of available tools, schemas, domains, constraints, and allowed playbooks.

## Integration Flows

## Evidence-first answers

Final responses must be based on tool outputs, document evidence, calculations, or explicitly stated limitations.

## Run trace as a trust layer

Each diagnostic run preserves the selected playbook, tool calls, parameters, outputs, and reasoning checkpoints for debugging and audit.

## Evidence and transparency approach

Developed the evidence and transparency approach: selected playbook, tool calls, parameters, tool results, execution timeline, run details, and JSON-level debug visibility.
