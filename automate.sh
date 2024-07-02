#!/bin/bash
from django.contrib.auth import get_user_model
from task_management.models import TaskModel


User = get_user_model()


u_1 = User.objects.get(id=1)


t_1 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 1', status='In Progress', priority='Low', category='UX Design')
t_2 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 2', status='In Progress', priority='Medium', category='UX Design')
t_3 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 3', status='In Progress', priority='High', category='UX Design')

t_4 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 4', status='Completed', priority='Low', category='Development')
t_5 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 5', status='Completed', priority='Medium', category='Development')
t_6 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 6', status='Completed', priority='High', category='Development')

t_7 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 7', status='Overdue', priority='Low', category='UX Design')
t_8 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 8', status='Overdue', priority='Medium', category='UX Design')
t_9 = TaskModel(assigned_to=u_1, description='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse aspernatur doloribus, recusandae eligendi sint animi ratione fugit maiores minima eveniet tempore possimus tempora omnis libero quis, saepe voluptatem tenetur modi?', title='Task No 9', status='Overdue', priority='High', category='UX Design')

t_1.save()
t_2.save()
t_3.save()
t_4.save()
t_5.save()
t_6.save()
t_7.save()
t_8.save()
t_9.save()

exit()
python manage.py runserver
