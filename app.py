from llama_index import download_loader, VectorStoreIndex, ServiceContext
from llama_index.llms import MistralAI
from dotenv import load_dotenv

load_dotenv()
URL = "https://en.wikipedia.org/wiki/Abraham_Lincoln"

# NOTE: "SimpleWebPageReader" is no longer exported from llama_index, using an alternative data loader
BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
loader = BeautifulSoupWebReader()
documents = loader.load_data(urls=[URL])

service_context = ServiceContext.from_defaults(llm=MistralAI())

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(service_context=service_context)

query = "What is this web page about?"
print(f"QUERY:\n{query}")
response = query_engine.query("What is this web page about?")
print(f"RESPONSE:\n{response}")

query = "What is one interesting fact about Abraham Lincoln?"
print(f"QUERY:\n{query}")
response = query_engine.query(query)
print(f"RESPONSE:\n{response}")
