import os

def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command

class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_BOT', 'start')
        self.CancelMirror = getCommand('CANCEL_BOT', 'cancel')
        self.CancelAllCommand = getCommand('CANCEL_ALL_BOT', 'cancelall')
        self.ListCommand = getCommand('LIST_BOT', 'list')
        self.StatusCommand = getCommand('STATUS_BOT', 'status')
        self.AuthorizedUsersCommand = getCommand('USERS_BOT', 'users')
        self.AuthorizeCommand = getCommand('AUTH_BOT', 'auth')
        self.UnAuthorizeCommand = getCommand('UNAUTH_BOT', 'unauth')
        self.AddSudoCommand = getCommand('ADDSUDO_BOT', 'addsudo')
        self.RmSudoCommand = getCommand('RMSUDO_BOT', 'rmsudo')
        self.RestartCommand = getCommand('RESTART_BOT', 'restart')
        self.StatsCommand = getCommand('STATS_BOT', 'stats')
        self.HelpCommand = getCommand('HELP_BOT', 'help')
        self.LogCommand = getCommand('LOG_BOT', 'logs')
        self.CloneCommand = getCommand('CLONE_BOT', 'clone')
        self.CountCommand = getCommand('COUNT_BOT', 'count')
        self.DeleteCommand = getCommand('DELETE_BOT', 'del')

BotCommands = _BotCommands()
