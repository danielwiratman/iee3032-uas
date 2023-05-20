from django.contrib import admin

from .models import Sensor, SensorLog, Actuator, ActuatorLog

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "value")
    
@admin.register(SensorLog)
class SensorLogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "value", "time")
    
@admin.register(Actuator)
class ActuatorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "state")
    
@admin.register(ActuatorLog)
class ActuatorLogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "state", "time")

