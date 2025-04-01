from promptflow.client import PFClient

client = PFClient()

run_results = client.run(
    flow="my_flow.yaml",
    data="data.jsonl",
)

for run_result in run_results:
    print(run_result.output["response"])
