def add_time(start, duration, dayShow = "NO"):

  carry_hours = 0
  carry_days = 0

  days_master_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  # print(days_master_list[1])   #test output to make sure list is constructed properly

  # get time from start string

  start_hours_end = start.find(":")
  start_hours = int(start[0:start_hours_end])

  # print(start_hours) #test output to ensure start hours captured correctly

  start_minutes_end = start.find(" ")
  start_minutes = int(start[start_hours_end+1:start_minutes_end])

  # print(start_minutes) # test output to ensure start minutes captured correctly

  am_pm = (start[start_minutes_end+1:-1])
  am_pm = am_pm + start[-1]

  # print(am_pm) #test output to ensure am_pm captured correctly

  # get added time from duration string

  duration_hours_end = duration.find(":")
  duration_hours = int(duration[0:duration_hours_end])

  # print(duration_hours) #test output to ensure duration hours calculated correctly

  duration_minutes = (duration[duration_hours_end+1:-1])
  duration_minutes = duration_minutes + duration[-1]

  # print(duration_minutes) #test output to ensure duration minutes calculated correctly

  # perform hours conversion for am / pm

  calc_hours = int(start_hours)

  if am_pm == "PM":
    calc_hours = calc_hours + 12
    # print("Start hours converted to 24 hour time:",calc_hours) # test output to ensure 24 hour time calculated correctly

  # perform minutes addition

  total_minutes = int(start_minutes) + int(duration_minutes)
  # print("Total minutes:",total_minutes) # test output to ensure total duration minutes calculated correctly

  # calculate carry over hours

  if total_minutes > 60:
    carry_hours = total_minutes // 60
    displayed_minutes = total_minutes - (carry_hours*60)
    # print("Displayed minutes:",displayed_minutes) # test output to ensure displayed minutes will be correct
  else:
    displayed_minutes = total_minutes
    # print("Displayed minutes:",displayed_minutes) # test output to ensure displayed minutes will be correct

  # perform hours addition

  total_hours = calc_hours + duration_hours + carry_hours
  # print("Total hours:",total_hours) # test output to ensure total hours calculated correctly

  #perform carry over days

  if total_hours > 24:
    carry_days = total_hours // 24
    new_hours = total_hours - (carry_days*24)
    # print("Displayed hours",new_hours) # test output to ensure new displayed hour is correct
    # print("Carried Days:",carry_days) # test output to ensure carried days forward is correct
  else:
    new_hours = total_hours

  # convert displayed hours back to 12 hour format and determine AM / PM flag variable

  if new_hours == 12:
    displayed_hours = "12"
    displayed_am_pm = "PM"
  elif new_hours == 0:
    displayed_hours = "12"
    displayed_am_pm = "AM"
  elif new_hours >=13 and new_hours <= 23:
    displayed_hours = new_hours % 12
    displayed_am_pm = "PM"
  else:
    displayed_hours = new_hours
    displayed_am_pm = "AM"

  # determine days later

  if carry_days >= 2:
    days_later = " (" + str(carry_days) + " days later)"
  elif carry_days == 1:
    days_later = " (next day)"
  else:
    days_later = ""
  # print(days_later, " days later") # test output to ensure number of days later calculated correctly

  # determine day of week which may need to be shown

  if dayShow !="NO":
    # print("Day will be shown") # test output to confirm day will be shown
    day_find = dayShow.lower()
    if day_find in days_master_list:
      day_index = days_master_list.index(day_find)
    # print("Day index is:", day_index) # test output to ensure correct day index is found
    if carry_days + day_index <= 6:
      new_day_index = int(carry_days + day_index)
      # print("New Day Index is:", new_day_index) # test output to ensure new correct day index found
      # print("New Day is:", days_master_list[new_day_index]) # test output to ensure new day is correct
    else:
      new_day_index = int((carry_days + day_index) % 7)
      # print("New Day Index is:", new_day_index) # test output to ensure correct day index found
      # print("New Day is:", days_master_list[new_day_index].capitalize()) #test output to ensure new day is correct
    
    # print output in format specified by rules with day shown

    new_time = str(displayed_hours) + ":" + str(displayed_minutes).zfill(2) + " " + displayed_am_pm + ", " + days_master_list[new_day_index].capitalize() + days_later

  else:

    #print output in format specified by rules without day shown

    new_time = str(displayed_hours) + ":" + str(displayed_minutes).zfill(2) + " " + displayed_am_pm + days_later

  # return new_time string to calling function

  return new_time
