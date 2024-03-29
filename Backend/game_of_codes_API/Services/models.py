from django.db import models


class Word(models.Model):
    word_text = models.CharField('Word', max_length=150, primary_key=True)

    def __str__(self):
        return self.word_text


class Agent(models.Model):
    PLAYER_OR_GUIDE = (
        ('P', 'Player'),
        ('G', 'Guide')
    )
    name = models.CharField('Name', max_length=150, primary_key=True)
    player_or_guide = models.CharField(max_length=1, choices=PLAYER_OR_GUIDE)
    num_of_wins = models.IntegerField('Number of Wins', default=0)
    num_of_losses = models.IntegerField('Number of Losses', default=0)
    total_games = models.IntegerField('Number of Games', default=0)

    num_of_single_wins = models.IntegerField('Number of Single Mode Wins', default=0)
    num_of_single_losses = models.IntegerField('Number of Single Mode Losses', default=0)
    total_single_games = models.IntegerField('Number of Single Mode Games', default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    BLUE_RED = (
        ('B', 'Blue'),
        ('R', 'Red'),
        ('Null', 'No one')
    )

    is_completed = models.BooleanField(default=False)
    blue_player = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='blue_player')
    red_player = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='red_player')
    blue_guide = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='blue_guide')
    red_guide = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='red_guide')

    blue_wrong_guesses = models.IntegerField(default=0)
    blue_correct_guesses = models.IntegerField(default=0)
    red_wrong_guesses = models.IntegerField(default=0)
    red_correct_guesses = models.IntegerField(default=0)

    winner = models.CharField(max_length=4, choices=BLUE_RED, default='Null')

    num_of_blue_words = models.IntegerField(default=8)
    num_of_red_words = models.IntegerField(default=8)

    is_blue_first = models.BooleanField(default=True)
    is_single_mode = models.BooleanField(default=False)


class Game_Square(models.Model):
    BLUE_RED_GREY_PURPLE = [
        ('B', 'Blue'),
        ('R', 'Red'),
        ('G', 'Green'),
        ('P', 'Purple')
    ]
    word = models.ForeignKey(Word, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    color = models.CharField(max_length=1, choices=BLUE_RED_GREY_PURPLE)
    is_guessed = models.BooleanField(default=False)


class Clue(models.Model):
    BLUE_RED = (
        ('B', 'Blue'),
        ('R', 'Red')
    )
    GOOD_OR_BAD = (
        (-1, 'Not Verified'),
        (0, 'Found All Hints'),
        (1, 'Chose Grey'),
        (2, 'Passed'),
        (3, 'Chose Opponent Colour'),
        (4, 'Chose Purple'),
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    agent_guide = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent_guide')
    agent_player = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent_player')
    badness = models.IntegerField(choices=GOOD_OR_BAD)
    clue_text = models.CharField('Clue', max_length=150)
    words_hinted = models.ManyToManyField(Game_Square, related_name='words_hinted')
    words_guessed = models.ManyToManyField(Game_Square, related_name='words_guessed')
    color = models.CharField(max_length=1, choices=BLUE_RED)
    num_of_words_hinted = models.IntegerField()
    num_of_words_correctly_guessed = models.IntegerField(default=0)

