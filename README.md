# Blogmaker

This is an ultra-simple self-hosted blog publishing solution.

### Dependencies

* pandoc (USE BREW TO INSTALL PANDOC)
* rsync

### How to use

See the [posts](./posts) directory for what a post should look like. Posts must be written in [markdown](https://daringfireball.net/projects/markdown/syntax), and filenames must end in ".md". Dates must be in (yyyy/mm/dd) format. All posts must be in the posts directory.

If you need a post to use MathJaX to format LaTeX equations, add the line

```
[pandoc]: <> (--mathjax)
```

to the config at the top of the post.

After writing the post in markdown, go to publish_article.py, and simpy change the name at the top of the file to whatever you decided to name the post (minus the '.md'. Run the file and you're good to go!).

### Misc

Credit to https://hackmd.io for CSS styles.
