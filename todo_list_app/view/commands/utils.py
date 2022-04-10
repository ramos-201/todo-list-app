from datetime import datetime


def show_task(text, tasks):
    print(f'\n::: {text}')
    for _, task in tasks.items():
        print(f'\n\tID          : {task.id}'
              f'\n\tTitle       : {task.title}'
              f'\n\tDescription : {task.description}'
              f'\n\tDeadline    : {task.deadline}'
              f'\n\tStatus      : {task.status}'
              f'\n\tCreated     : {task.created}'
              f'\n\tModified    : {task.modified}')


def get_deadline():
    while True:
        get_date = input('Deadline task - format (YYYY-MM-DD): ')
        format_date = '%Y-%m-%d'
        try:
            deadline = datetime.strptime(get_date, format_date)
        except ValueError:
            print(f'::: Invalid date format, expected: (YYYY-MM-DD)')
        else:
            today = datetime.now()
            if today.date() > deadline.date():
                print(f'::: Deadline is not valid with current date')
            else:
                break
    return deadline
