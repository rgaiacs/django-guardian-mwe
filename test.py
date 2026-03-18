from datetime import datetime

from django.contrib.auth.models import User

from guardian.shortcuts import assign_perm

from polls import models

u = User.objects.create(first_name="Jane", last_name="Doe",)

q = models.QuestionWithText.objects.create(question_text="Foo", pub_date=datetime.now(), answer="Bar",)

# This works.
assign_perm("view_questionwithtext", u, q)
assign_perm("change_questionwithtext", u, q)
assign_perm("delete_questionwithtext", u, q)

# This does NOT work.
assign_perm("answer", u, q)