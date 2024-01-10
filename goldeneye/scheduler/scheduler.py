import contextlib
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.core.management import call_command


def db_backup():
    with contextlib.suppress(Exception):
        call_command("dbbackup")


def start():
    scheduler = BackgroundScheduler()

    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        db_backup,
        "interval",
        minutes=1,
        jobstore="default",
        id="daily_backup",
        replace_existing=True,
    )

    register_events(scheduler)
    scheduler.start()


# def start():
#     scheduler = BackgroundScheduler()

#     scheduler.add_jobstore(DjangoJobStore(), "default")
#     job = scheduler.add_job(
#         db_backup,
#         "interval",
#         minutes=1,
#         jobstore="default",
#         id="daily_backup",
#         replace_existing=True,
#     )

#     print(f"Job added: {job}")

#     register_events(scheduler)
#     scheduler.start()
#     print("Scheduler started")
