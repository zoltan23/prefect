from prefect import flow, get_run_logger
from tasks import test_task

@flow
def main_flow():
    logger = get_run_logger()
    logger.info("Main flow called!")
    logger.info("This was created in branch main.")
    logger.info("This was created in branch main in GitHub.")

    test_task()

    return

if __name__ == '__main__':
    main_flow()
