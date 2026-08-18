from parsing.parse import Parse
from simulation import Simulation
from graph import Graph
from teste import Display
from hub import Hub
from colorama import init
import sys


class Main():

    @staticmethod
    def outstandard_color(start_end):
        if start_end[0]['color'] == 'outstandard':
            start_end[0]['color'] = '\x1b[0m'
            print('There is an outstandard color in "start_hub_color", the program will continue sticking with the regular terminal output color')
        if start_end[1]['color'] == 'outstandard':
            start_end[1]['color'] = '\x1b[0m'
            print('There is an outstandard color in "end_hub_color", the program will continue sticking with the regular terminal output color')


    @classmethod
    def main(cls):
        init(autoreset=True)

        Parse.duplicate_line('nb_drones:')
        Parse.duplicate_line('start_hub:')
        Parse.duplicate_line('end_hub:')

        if not Parse.first_line():
            sys.exit(1)

        nb_drones: int = Parse.get_nb_drones()
        start_end = Parse.splitting_form_lines()

        if not start_end:
            print('Empty input_file, wrong input file name or invalid syntax')
            sys.exit(1)
        if len(start_end) < 2:
            print('Invalid syntax in one or more lines on the first 3 lines in input_file, exitting the program')
            sys.exit(1)

        
        hubs: list[dict] = Parse.hubs_positions()

        start: Hub = Hub(
            name=start_end[0]['name'],
            position=start_end[0]['position'],
            color=start_end[0].get('color'),
            role='start',
        )
        end: Hub = Hub(
            name=start_end[1]['name'],
            position=start_end[1]['position'],
            color=start_end[1].get('color'),
            role='end',
        )
        middle: list[Hub] = [
            Hub(
                name=h['name'],
                position=h['position'],
                color=h.get('color'),
                zone=h.get('zone', 'normal'),
                max_drones=h.get('max_drones', 1),
                role='hub',
            )
            for h in hubs
        ]

        all_hubs: dict[str, Hub] = {h.name: h for h in [start, end] + middle}
        connections: list[dict] = Parse.get_connections()
        graph: Graph = Graph(all_hubs, connections)
        mapa: dict[str, Hub] = graph.build()
        
        # print('--- hubs ---')
        # for name, hub in mapa['hubs'].items():
        #     print(f'{name}: pos={hub.position}, zone={hub.zone}, cost={hub.cost}, max={hub.max_drones}')
            
        # print()
        # print('--- links ---')
        # for name, neighbors in mapa['links'].items():
        #     print(f'{name} -> {neighbors}')
        # print()
        
        path = Simulation.bfs(mapa, start.name, end.name)
        Display.display(path, all_hubs)
        

if __name__ == '__main__':
    try:
        Main.main()
    except Exception as e:
        print(f'Failed dummy\n{e}')

