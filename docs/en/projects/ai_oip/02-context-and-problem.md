# Context and Problem

## Context

Enterprise AI can help with synthesis, but a free-form chat over corporate data is a weak and unsafe model for managerial analytics.

In executive questions, the answer text is not enough. It also matters:

- which data the conclusion rests on;
- which calculation was performed;
- which documents were used;
- which limitations the analysis has;
- what is a fact and what is a hypothesis;
- why this diagnostic path was chosen.

This prototype explores how LLM-based managerial analytics could be made controlled, traceable, and useful for enterprise discussion.

## Problem

Typical executive analytics still requires manual assembly of a picture from BI reports, spreadsheets, task trackers, ITSM, PMO materials, documents, meeting notes, and domain experts.

LLMs can speed up synthesis, but unconstrained chat over corporate data creates risks:

- hallucination;
- wrong source selection;
- no reproducible calculation;
- no audit path for the conclusion;
- mixing facts and interpretation;
- unsafe model access to data.

The prototype was built to check a narrower idea: the LLM should not “answer from memory” and should not get direct access to business data. It should operate inside a controlled execution loop: select an allowed tool path, call backend tools, retrieve structured results, preserve a basic execution trace, and produce an evidence-backed answer.

The intended product direction remains an evidence-backed decision-support prototype for executives and domain owners. That direction was not delivered as a complete product in this work.
