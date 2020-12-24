# The Zen of Python, by Tim Peters

this = "Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.\
Flat is better than nested.\
Sparse is better than dense.\
Readability counts.\
Special cases aren't special enough to break the rules.\
Although practicality beats purity.\
Errors should never pass silently.\
Unless explicitly silenced.\
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch.\
Now is better than never.\
Although never is often better than *right* now.\
If the implementation is hard to explain, it's a bad idea.\
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those!"

better_count = this.count('better')
never_count = this.count('never')
is_count = this.count('is')
this_up = this.upper()
this_replace = this.replace('i', '&')


print (f"There is {better_count} times used \"better\",\
 {never_count} times \"never\",\
 and {is_count} times \"is\"\
 in \"The Zen of Python\".")

print (f"\nThat's how \"The Zen of Python\" looks, when you read it angry: \n\
{this_up}")

print (f"\nAnd let's replace \"i\" with \"&\" \n{this_replace}")