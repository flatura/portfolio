# Overview

## Summary

An enterprise AI prototype for evidence-based managerial analytics.

The product direction is an **AI Executive Analyst with verifiable evidence**: a decision-support layer that helps executives and domain owners investigate business questions, detect operational risks, explain deviations, and prepare management actions without relying on opaque AI reasoning.

## Technology Stack

**Agent runtime:** LangGraph, FastAPI, Python  
**Interface:** Open WebUI as temporary demo harness  
**Data layer:** PostgreSQL, Qdrant, MinIO, Redis  
**AI integration:** OpenAI-compatible LLM API, prompt-based workflow control  
**Architecture patterns:** Tool Gateway, Tool Registry, playbook-based diagnostics, RAG, semantic layer, run trace, evidence trail  
**Development approach:** AI-assisted prototyping, synthetic data generation, scenario-driven MVP validation