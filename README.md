# LSTE Plugin: Active Menu

This plugin for [Lauras Simple Template Engine (LSTE)](https://github.com/lauratheq/lste) modifies HTML content to mark the active menu item based on meta information. It is particularly useful for highlighting the current page in a navigation menu, providing a visual cue to users about their location on the site.

## Usage

### Installation

1. Add the plugin to your LSTE configiration by including it in your `.listerc` file:

```ini
[plugins]
active-menu = lauratheq/active-menu.lste
```

2. LSTE will automatically download and activate the plugin during the next site generation.

### Configuration

To use the Active Menu plugin, you need to add an `active-menu` meta field to your content files (e.g. `contact.md`).

```markdown
{{active-menu: contact}}

# Contact

Lorem ipsum dolor ...
```

In your HTML template, ensure that each menu item has an id attribute that matches the values you use in the active-menu field. For example:

```html
<ul>
    <li id="home"><a href="index.html">Home</a></li>
    <li id="about"><a href="about.html">About</a></li>
    <li id="contact"><a href="contact.html">Contact</a></li>
</ul>
```

The plugin will automatically add the active class to the relevant menu item based on the active-menu field:

```html
<ul>
    <li id="home"><a href="index.html">Home</a></li>
    <li id="about"><a href="about.html">About</a></li>
    <li class="active" id="contact"><a href="contact.html">Contact</a></li>
</ul>
```

## Contributing

### Contributor Code of Conduct

Please note that this project is adapting the [Contributor Code of Conduct](https://learn.wordpress.org/online-workshops/code-of-conduct/) from WordPress.org even though this is not a WordPress project. By participating in this project you agree to abide by its terms.

### Basic Workflow

* Grab an issue
* Fork the project
* Add a branch with the number of your issue
* Develop your stuff
* Commit to your forked project
* Send a pull request to the main branch with all the details

Please make sure that you have [set up your user name and email address](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) for use with Git. Strings such as `silly nick name <root@localhost>` look really stupid in the commit history of a project.

Due to time constraints, you may not always get a quick response. Please do not take delays personally and feel free to remind.

### Workflow Process

* Every new issue gets the label 'Request'
* Every commit must be linked to the issue with following pattern: `#${ISSUENUMBER} - ${MESSAGE}`
* Every PR only contains one commit and one reference to a specific issue
