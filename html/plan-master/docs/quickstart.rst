.. _quickstart:

Quickstart
==========

This page gives a good introduction to Plan.  If you do not have Plan
installed, check out :ref:`installation` section.


A Minimal Example
-----------------

A simple usage looks like this::
    
    from plan import Plan

    cron = Plan()

    cron.command('ls /tmp', every='1.day', at='12:00')
    cron.command('pwd', every='2.month')
    cron.command('date', every='weekend')

    if __name__ == '__main__':
        cron.run()

Just save it as `schedule.py` (or whatever you want) and run it with your
Python interpreter.  Make sure to not name it `plan.py` because it would
conflict with Plan itself.

Now we do not run with one explicit run_type, default run_type check will be
used, or you can just get your cron syntax content by access
:attr:`~plan.Plan.cron_content`, you should see your cron syntax jobs in the
output of terminal::
    
    # Begin Plan generated jobs for: main
    0 12 * * * ls /tmp
    0 0 1 1,3,5,7,9,11 * pwd
    0 0 * * 6,0 date
    # End Plan generated jobs for: main

It seems everything goes fine, we can write it to crontab now::
    
    if __name__ == '__main__':
        cron.run('write')


Explanation
-----------

So what did the above code do?

1. First we imported the :class:`~plan.Plan` class.  An instance of this
   class will be one group of cron jobs.
2. Next we create an instance of this class.  We are not passing any arguments
   here, though, the first argument is the name of this group of cron jobs.
   In our case, we have the default name 'main' here.  For more information
   have a look at the :ref:`plan_definition` documentation.
3. We then use the :meth:`~plan.Plan.command` to register three command jobs on
   this Plan object.
4. Finally we run this Plan object and check your cron syntax jobs or write
   it to your crontab, see :ref:`run_types` for more details.
