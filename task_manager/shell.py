from manager.models import Task
from datetime import datetime

task1 = Task.objects.create(name="zrobic koalcje", description="pożywna i staropolskia", date_created=datetime.now(), importance=False)
task2 = Task.objects.create(name="zrobic zakupy", description="warzywa w Lidlu i miesny", date_created=datetime.now(), importance=True)
task3 = Task.objects.create(name="posprzatać kuchnie", description="wymienic zapach w zmywarce", date_created=datetime.now(), importance=False)
task4 = Task.objects.create(name="odebrac poczte", description="na cito!", date_created=datetime.now(), importance=True)
