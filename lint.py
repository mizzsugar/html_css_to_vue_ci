import os
import pathlib


def _html_to_vue(target_file: pathlib.PosixPath) -> None:
    written = pathlib.Path(f'./_dest/{target_file}.vue')
    written.parent.mkdir(parents=True, exist_ok=True)
    with target_file.open() as r:
        with written.open(mode='w') as w:
            w.write('<template>\n')
            for line in r.readlines():
                if '<!doctype html>' in line:
                    continue
                if line == '\n':
                    w.write(line)
                    continue
                w.write(f'  {line}')
            w.write('</template>\n')  


def _css_to_vue(target_file: pathlib.PosixPath) -> None:
    written = pathlib.Path(f'./_dest/{target_file}.vue')
    written.parent.mkdir(parents=True, exist_ok=True)
    with target_file.open() as r:
        with written.open(mode='w') as w:
            w.write(
                '<template>\n'
                '  <div />\n'
                '</template>\n'
                '<style>\n'
            )
            for line in r.readlines():
                w.write(line)
            w.write('</style>\n')


def main() -> None:
    for html_file in pathlib.Path('.').glob('**/*.html'):
        _html_to_vue(html_file)

    for css_file in pathlib.Path('.').glob('**/*.css'):
        _css_to_vue(css_file)


if __name__ == '__main__':
    main()
