import ipywidgets as widgets
from IPython.display import display, HTML
import verticapy as vp
import pandas as pd

class VerticaViewer:
    def __init__(self):
        # Create connection input widgets
        self.host_input = widgets.Text(
            description='Host:',
            placeholder='Enter host',
            style={'description_width': 'initial'}
        )
        
        self.port_input = widgets.Text(
            description='Port:',
            placeholder='5433',
            value='5433',
            style={'description_width': 'initial'}
        )
        
        self.database_input = widgets.Text(
            description='Database:',
            placeholder='Enter database name',
            style={'description_width': 'initial'}
        )
        
        self.username_input = widgets.Text(
            description='Username:',
            placeholder='Enter username',
            style={'description_width': 'initial'}
        )
        
        self.password_input = widgets.Password(
            description='Password:',
            placeholder='Enter password',
            style={'description_width': 'initial'}
        )
        
        self.connect_button = widgets.Button(
            description='Connect',
            button_style='primary'
        )
        self.connect_button.on_click(self.connect_to_database)
        
        # Create table viewing widgets
        self.table_input = widgets.Text(
            description='Table:',
            placeholder='Enter table name',
            style={'description_width': 'initial'}
        )
        
        self.view_button = widgets.Button(
            description='View Table',
            button_style='success',
            disabled=True
        )
        self.view_button.on_click(self.view_table)
        
        # Status output
        self.output = widgets.Output()
        
        # Layout
        self.connection_box = widgets.VBox([
            widgets.HTML("<h3>Database Connection</h3>"),
            self.host_input,
            self.port_input,
            self.database_input,
            self.username_input,
            self.password_input,
            self.connect_button
        ])
        
        self.viewer_box = widgets.VBox([
            widgets.HTML("<h3>Table Viewer</h3>"),
            self.table_input,
            self.view_button
        ])
        
        self.main_layout = widgets.VBox([
            self.connection_box,
            self.viewer_box,
            self.output
        ])
        
    def connect_to_database(self, b):
        with self.output:
            self.output.clear_output()
            try:
                conn_info = {
                    'host': self.host_input.value,
                    'port': self.port_input.value,
                    'database': self.database_input.value,
                    'user': self.username_input.value,
                    'password': self.password_input.value
                }
                
                vp.new_connection(
                    conn_info,
                    auto=True,
                    overwrite=True,
                )
                print("Successfully connected to database!")
                self.view_button.disabled = False
                
            except Exception as e:
                print(f"Error connecting to database: {str(e)}")
                self.view_button.disabled = True
    
    def view_table(self, b):
        with self.output:
            self.output.clear_output()
            try:
                table_name = self.table_input.value
                if not table_name:
                    raise ValueError("Please enter a table name")
                
                df = vp.vDataFrame(table_name)
                display(df.head().to_pandas())
                print(f"\nShowing first 5 rows of table: {table_name}")
                
            except Exception as e:
                print(f"Error viewing table: {str(e)}")
    
    def display(self):
        display(self.main_layout)