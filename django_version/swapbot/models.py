
class person(models.Model):
  id = models.IntegerField(null=False,default=val)
  name = models.CharField(max_length=L,null=False,default=val)
  phone = models.CharField(max_length=L,null=True,default=val)
  email = models.CharField(max_length=L,null=False,default=val)
  pasword = models.CharField(max_length=L,null=False,default=val)
  loc_id = models.IntegerField(null=True,default=val)
  is_activated = models.IntegerField(null=False,default=val,primary_key=True)
  loc_id = models.null=True,default=val)

class donation(models.Model):
  id = models.IntegerField(null=False,default=val)
  item_id = models.ForeignKey(itemtype)
  size = models.CharField(max_length=L,null=True,default=val)
  donor_id = models.ForeignKey(null=False,default=val,primary_key=True)

class donor(models.Model):
  #was trying to figure out djano subclass vs foreign key for 
  id = models.ForeignKey(Person)
  forget what point of donor id_2 was... 
  id_2 = models.null=True,default=val)

class recipient(models.Model):
  id = models.ForeignKey(person) #models.IntegerField(null=False,default=val)
  middleManID = models.ForeignKey(person)
  #id_2 = models.null=True,default=val)

class middleman(models.Model):
  #was trying to figure out djano subclass vs foreign key for 
  id = models.ForeignKey(Person) 
  #.IntegerField(null=False,default=val)

class itemtype(models.Model):
  id = models.IntegerField(null=False,default=val)
  item = models.CharField(max_length=L,null=False,default=val)
  mwc = models.CharField(max_length=L,null=False,default=val)
  imagePath = models.CharField(max_length=L,null=False,default=val)
  estimatedPrice = models.DecimalField(max_digits=None, decimal_places=Nonenull=False,default=val,primary_key=True)

class location(models.Model):
  id = models.IntegerField(null=False,default=val)
  lat = models.CharField(max_length=L,null=False,default=val)
  long = models.CharField(max_length=L,null=False,default=val)
  street_addr = models.CharField(max_length=L,null=False,default=val,primary_key=True)


class open_hors(models.Model):
  loc_id = models.ForeignKey(location)#models.IntegerField(null=False,default=val)
  open_hour = models.TimeField(null=False,default=val)
  close_hour = models.TimeField(null=False,default=val)
  day_of_week = models.CharField(max_length=L,null=False,default=val)

class request(models.Model):
  id = models.IntegerField(null=False,default=val)
  item_id = models.ForeignKey(itemtype) #IntegerField(null=False,default=val)
  size = models.CharField(max_length=L,null=True,default=val)
  recipient_id = models.ForeignKey(recipient) #IntegerField(null=False,default=val)
  state = models.IntegerField(null=False,default=val,primary_key=True)
  #item_id = models.null=True,default=val)
  #recipient_id = models.null=True,default=val)
  #item_id_2 = models.null=True,default=val)

class swap(models.Model):
  id = models.IntegerField(null=False,default=val)
  don_id = models.ForeignKey(donor)#IntegerField(null=False,default=val)
  req_id = models.ForeignKey(recipient)#IntegerField(null=False,default=val)
  create_time = models.DateTimeField(auto_now=True null=True,default=val)
  close_time = models.DateTimeField(auto_now=True null=True,default=val)
  sch_time = models.DateTimeField(auto_now=True null=True,default=val)
  state = models.CharField(max_length=L,null=False,default=val,primary_key=True)
  #don_id = models.null=True,default=val)
  #req_id = models.null=True,default=val)
