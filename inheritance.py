# Defines class Parent.
class Parent(object):

    # Defines function override().
    def override(self):
        print "PARENT override()"

    # Defines function implicit().
    def implicit(self):
        print "PARENT implicit()"

    # Defines function altered().
    def altered(self):
        print "PARENT altered()"

# Defines class Child. Inherits from Parent().
class Child(Parent):

    # Overrides Parents function override().
    def override(self):
        print "CHILD override()"

    # Overrides and alters Parents function altered().
    def altered(self):
        """Dingle"""
        print "CHILD, BEFORE PARENT altered()"
        # Calls function altered() in super class (Parent).
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
