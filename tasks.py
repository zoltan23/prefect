from prefect import task, get_run_logger

@task
def test_task():
    logger = get_run_logger()
    logger.info("test_task called!")
    
    return 