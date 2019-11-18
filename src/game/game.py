from random import randint
from random import choice
import os

def cli():
    while True:
        choice(games)()
        try:
            assert input("\n\nDo you want to play again? \n\n")[0].lower() == "y"
        except:
            break
        os.system('cls')


def guess():
    x=randint(0,9)
    while True:
        try:
            guess=int(input(f"\nGuess the number between 0 and 9. "))
            assert guess==x
        except:
            if guess>x:
                print(f"\n{guess} is too high! Guess again. ")
            else:
                print(f"\n{guess} is too low! Guess again. ")
            continue
        print(f"\nCorrect! The number is {x}. ")
        break


def name():
    n = input('Please enter your name: ')
    print(f"Hello, {n}!")


def add():
    x,y=randint(0,5),randint(0,5)
    while True:
        try:
            assert int(input(f"\nWhat is {x}+{y}? "))==x+y
        except:
            print("\nIncorrect. Try again! ")
            continue
        print(f"\nCorrect! {x}+{y} is {x+y}. ")
        break


def hangman():
    chance = 10
    word = choice(words)
    board = len(word) * ["_"]
    while chance:
        if "".join(board) == word:
            print("\n\nYOU WIN!!!\n\n")
            break
        print(f"You have {chance} chances left to guess the word:\n")
        print(f"{' '.join(board)}\n\n")
        guess = input("Guess a letter: ")
        if guess in word:
            board[word.index(guess)] = guess
        else:
            chance -= 1
            input(f"Sorry! '{guess}' is not in the word.")
        os.system("cls")
    else:
        print(f"That was your last chance. The word is '{word}'.\n\nGame Over")


words = """
a
came
had
make
people
ten
walk
all
can
has
many
play
than
want
am
come
have
me
please
thank
was
an
day
he
more
pretty
that
we
and
did
her
much
purple
the
were
any
do
here
must
put
them
what
are
down
hers
my
ran
then
when
as
eat
him
new
red
there
where
ask
eight
his
nice
run
these
which
at
find
how
nine
said
they
white
ate
five
if
no
saw
thing
who
away
for
in
not
say
this
why
be
four
into
now
see
three
with
because
from
is
of
seven
to
went
been
get
it
on
she
too
work
before
girl
jump
one
six
two
yellow
big
go
like
only
small
up
yes
black
going
little
or
so
very
you
blue
good
look
orange
some
 
your
boy
great
 
other
soon
 
 
brown
green
 
our
 
 
 
but
 
 
out
 
 
 
by
 
 
over
""".split()


games = [add, guess, name, hangman]


if __name__ == "__main__":
    cli()