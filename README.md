# LlamaIndex Example Project README

## Overview

This example project demonstrates how to use the `llama_index` library for indexing and querying web content. In this project, we use the `BeautifulSoupWebReader` as a data loader to extract information from a web page, specifically the Wikipedia page of Abraham Lincoln. We then create a VectorStoreIndex and use it for querying specific information.

## Requirements

- Python 3.x
- `llama_index`
- `dotenv`

## Setup

1. Install the required libraries:

   ```bash
   pip install llama_index python-dotenv
   ```

2. Set up the `.env` file at the root of your project with the following keys:

   ```plaintext
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   MISTRAL_API_KEY=YOUR_MISTRAL_API_KEY
   ```

   Replace `YOUR_OPENAI_API_KEY` and `YOUR_MISTRAL_API_KEY` with your respective API keys.

3. Load environment variables:

   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

## Usage

1. Define the URL for data loading:

   ```python
   URL = "https://en.wikipedia.org/wiki/Abraham_Lincoln"
   ```

2. Use `BeautifulSoupWebReader` to load the document:

   ```python
   BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
   loader = BeautifulSoupWebReader()
   documents = loader.load_data(urls=[URL])
   ```

3. Create and use the VectorStoreIndex for querying:

   ```python
   from llama_index import VectorStoreIndex, ServiceContext
   from llama_index.llms import MistralAI

   service_context = ServiceContext.from_defaults(llm=MistralAI())
   index = VectorStoreIndex.from_documents(documents)
   query_engine = index.as_query_engine(service_context=service_context)

   query = "What is this web page about?"
   response = query_engine.query(query)
   print(f"RESPONSE:\n{response}")
   ```

4. Example of querying an interesting fact:

   ```python
   query = "What is one interesting fact about Abraham Lincoln?"
   response = query_engine.query(query)
   print(f"RESPONSE:\n{response}")
   ```

## Notes

- The `SimpleWebPageReader` is no longer available in `llama_index`. Use `BeautifulSoupWebReader` as an alternative.
- Ensure you have a valid `.env` file with necessary configurations.
