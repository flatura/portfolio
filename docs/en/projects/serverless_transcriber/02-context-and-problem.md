# Context and Problem

## Context and Background

## Context and Problem

There is an episodic need to transcribe long audio recordings: interviews, work discussions, calls, notes, and research materials. A typical file can run 1.5+ hours and weigh hundreds of megabytes.

Ready-made SaaS services solve the task, but for a personal/limited scenario they provide excessive functionality, opaque pricing, and extra operational overhead: the user manually uploads a file, waits for processing, downloads the result, and stores it separately.

## Problem

The key architectural problem: transcription is a long asynchronous operation, and audio files are too large for direct transfer through API Gateway/Lambda. Therefore the system must separate upload, processing start, webhook receipt, result storage, and transcript download.

Some recordings may contain private information, so it is important to restrict access to the interface, files, and results. At the same time, sending audio to an external transcription provider remains a deliberate trade-off accepted for cost, quality, and lack of owned GPU infrastructure.
