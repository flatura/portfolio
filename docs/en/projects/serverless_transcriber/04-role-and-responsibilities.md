# Role and Responsibilities

## My Role

I acted as the system designer and technical owner of the solution.

My work included:

- translating a personal need into requirements, constraints, and an architectural model;
- choosing a serverless architecture given episodic load and cost constraints;
- designing the asynchronous process: upload -> transcription request -> webhook -> result storage -> download;
- designing the transcription job state model;
- selecting AWS services and responsibility boundaries between Lambda, S3, DynamoDB, API Gateway, Cognito, and the external transcription provider;
- documenting sequence diagrams and ADRs;
- using AI-assisted development tools as an implementation accelerator while keeping manual control over architecture, security boundaries, and deployment decisions.

## AI Usage

The project was developed with AI assistance.

LLMs were used to accelerate implementation, generate boilerplate code, and iterate quickly. Key decisions remained under manual control:

* requirements interpretation;
* domain modeling;
* architecture decisions;
* data boundaries;
* access model;
* code review;
* debugging;
* deployment decisions;
* technical documentation.
