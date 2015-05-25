ansible
=======

This repository is my personal Ansible repository for configuring my home
servers.


Roles
-----

- *baseline*: a usable baseline for servers. Sets up networking, ntp, sshd,
  sudo, and user accounts. Also installs some nice-to-have utilities: zsh,
  grml's zsh configuration, tmux, htop, and vim. Sets up a basic configuration
  for tmux and vim.
- *docker*: installs and configures docker. Optionally sets up docker containers
  based on what containers are defined in the `docker_run` variable.
- *firewall*: a simple iptables-based stateful firewall. Based on the
  [instructions](https://wiki.archlinux.org/index.php/Simple_stateful_firewall)
  on the ArchWiki.
- *haproxy*: installs and configures haproxy.
- *update*: updates all installed packages on all hosts.
