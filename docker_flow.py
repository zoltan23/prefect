from prefect import flow, get_run_logger

# This was created in test.
# This was created in test 2.
# This was created in test 3.
# This was created in main.
# This was created in test 4.
# This was done in GitHub.

@flow
def docker_flow():
    logger = get_run_logger()
    logger.info("Prefect In Docker Container????")

if __name__ == '__main__':
    docker_flow()
