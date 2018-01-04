import argparse
import csv
from newspaper import Article
from newspaper.article import ArticleException


def enhance(source_filepath, dest_filepath):
    with open(source_filepath, encoding='utf-8') as csv_source, open(dest_filepath, 'w', encoding='utf-8') as csv_dest:
        reader = csv.DictReader(csv_source)
        fieldnames = reader.fieldnames
        fieldnames.append('text')
        writer = csv.DictWriter(csv_dest, fieldnames=fieldnames)
        writer.writeheader()
        for count, row in enumerate(reader):
            print(count+1)
            row['text'] = get_text(row['url'])
            writer.writerow(row)


def get_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except ArticleException:
        return ''

if __name__ == '__main__':
    parser = argparse.ArgumentParser("")
    parser.add_argument('source_file')
    parser.add_argument('dest_file')

    args = parser.parse_args()
    enhance(args.source_file, args.dest_file)
