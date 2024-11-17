from prefect import flow, get_run_logger

# This was created in test.

@flow
def docker_flow():
    logger = get_run_logger()
    logger.info("Prefect In Docker Container????")

if __name__ == '__main__':
    docker_flow()