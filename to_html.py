#!/usr/bin/env python3
import json
import sys
import textwrap

template = open('template.html').read()

if __name__ == '__main__':
    assert len(sys.argv) == 2, 'pass filename.jsonlines'
    days = {}
    for jsonline in open(sys.argv[1], 'r'):
        day = json.loads(jsonline)
        days[day['date']] = day
    body = ''
    for date, day in sorted(days.items(), reverse=True):
        html = textwrap.dedent('''
            <h1>{date}</h1>
            <pre>
            date: {date}
            url: {url}
            file_urls:
                {file_urls[0]}
                {file_urls[1]}
            langsam_url: {langsam_url}
            langsam_filename: {langsam_filename}
            originaltempo_url: {originaltempo_url}
            originaltempo_filename: {originaltempo_filename}
            </pre>
            <p>
                <audio controls preload="none">
                  <source src="mp3/{date}.mp3" type="audio/mp3">
                </audio> langsam
                <br>
                <audio controls preload="none">
                  <source src="mp3/orig/{date}.mp3" type="audio/mp3">
                </audio> originaltempo
            </p>
            <p>{html}</p>
        ''')
        body += html.format(**day)
    with open('lgn.html', 'w') as fw:
        fw.write(template % dict(body=body))

