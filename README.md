# article-text
Enhances a CSV with article text retrieved using Newspaper3k

[Newspaper3k](https://github.com/codelucas/newspaper/) does all of the heavy lifting.

## Setup

    pip install newspaper3k
    
## Usage

    python enhance_text.py <source file> <destination file>
    
The source file must be a CSV containing a `url` column containing the URL of each article.

`enhance_text.py` will retrieve the article, extract text, and add to a new column called `text`.
All other columns will be preserved.