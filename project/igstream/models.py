from django.db import models



# Create your models here.
class Epic(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=64)

class Chart(models.Model):
    ltv = models.IntegerField()
    ttv = models.IntegerField()
    utm = models.IntegerField()
    day_open_mid = models.FloatField()
    day_net_chg_mid = models.FloatField()
    day_perc_chg_mid = models.FloatField()
    day_high = models.FloatField()
    day_low = models.FloatField()
    ofr_open = models.FloatField()
    ofr_high = models.FloatField()
    ofr_low = models.FloatField()
    ofr_close = models.FloatField()
    bid_open = models.FloatField()
    bid_high = models.FloatField()
    bid_low = models.FloatField()
    bid_close = models.FloatField()
    ltp_open = models.FloatField()
    ltp_high = models.FloatField()
    ltp_low = models.FloatField()
    ltp_close = models.FloatField()
    cons_end = models.BooleanField()
    cons_tick_count = models.IntegerField()
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
