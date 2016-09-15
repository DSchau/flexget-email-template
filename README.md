# Flexget email template (WIP)

A simple template intended to be used with the [email][flexget-email] plugin available in flexget.

## Instructions

1. Create a folder (if it does not already exist) `templates` in the same directory as the `config.yml` file
 - For instance: `~/.flexget/templates/`
1. Copy `dist/html-dschau.template` to the `templates` folder
1. Configure an e-mail task in your config.yml, consider [my task][flexget-email-task]
 - Consider testing the task with `flexget execute --task taskname`

[flexget-email]: http://flexget.com/Plugins/email
[flexget-email-task]: https://github.com/DSchau/flexget-config/blob/master/config.yml#L94-L112
