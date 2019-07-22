from cloudshell.cli.service.command_mode import CommandMode

# new line or begin of the line that doesn't saved in match
BEGIN_LINE_PATTERN = r"((?<=\n)|^)"


class EnableCommandMode(CommandMode):
    PROMPT = (
        rf"{BEGIN_LINE_PATTERN}"
        r"((?!\(config.*?\))(\w|-|\(|\)))*"  # \w or - or () and without (config.*)
        r"#\s*$"
    )
    ENTER_COMMAND = ""
    EXIT_COMMAND = "exit"

    def __init__(self):
        super().__init__(self.PROMPT, self.ENTER_COMMAND, self.EXIT_COMMAND)


class ConfigCommandMode(CommandMode):
    PROMPT = rf"{BEGIN_LINE_PATTERN}\S+\(config\)#\s*$"
    ENTER_COMMAND = "config"
    EXIT_COMMAND = "exit"

    def __init__(self):
        super().__init__(self.PROMPT, self.ENTER_COMMAND, self.EXIT_COMMAND)


CommandMode.RELATIONS_DICT = {EnableCommandMode: {ConfigCommandMode: {}}}
