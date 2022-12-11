from django import template
from ..models import UserInfo

register = template.Library()


@register.filter
def IndexAccess(userKey, arg):
    return userKey[arg]

@register.filter
def rangeAccess2(userKey, arg):
    return userKey[:arg]

@register.filter
def getcurrentUser(userKey):
    return UserInfo.objects.get(correspond_user = userKey)

@register.filter
def checkAlreadyFriend(userKey, arg):
    current_user = UserInfo.objects.get(correspond_user = userKey)
    friend_idList = [friend.pk for friend in current_user.friends.all()]

    if int(arg) in friend_idList:
        return True
    else:
        return False

#This simple_tag is created because I cannot figure out how to pass the result of a filter (i.e. IndexAccess) to
#another filter (i.e. checkAlreadyFriend).I came in contact with the concept of "tag" after already creating "filter"
# functions here, and I am not sure what's the exact advantages and disadvantages of each. I decide not to remove
# the "IndexAccess" filter above because I don't want to modify existing codes that are supposedly already working
# and risk introducing unexpected problems. I might do it near the end of the project for optimization purposes, but
# I decide to stick with both the tag function below and the filter function above at this time even though they are
# doing effectively the same thing. (10/30/2022 -- Yuanzhan Gao)
@register.simple_tag
def accessLastElement(userName):
    return userName[-1]


@register.simple_tag
def instructorParse_Name(instructor):
    instructor = instructor.replace("{", "")
    instructor = instructor.replace("}", "")
    instructor_parsed = instructor.split(",")
    name_parsed = instructor_parsed[0].split(":")
    name = name_parsed[1].replace("'", "")
    return name


@register.simple_tag
def instructorParse_Email(instructor):
    instructor = instructor.replace("{", "")
    instructor = instructor.replace("}", "")
    instructor_parsed = instructor.split(",")

    email_parsed = instructor_parsed[1].split(":")
    email = email_parsed[1].replace("'", "")

    return email
