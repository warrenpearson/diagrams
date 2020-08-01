import yaml
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.database import Mssql


client_config = "./client.yml"

with open(client_config, 'r') as stream:
    config = yaml.load(stream, Loader=yaml.SafeLoader)
    client = config['client']
    show_file = config['show_file']

with Diagram("Example Architecture", show=show_file, direction="LR"):
    vpc = Cluster(f"{client} Virtual Private Cloud")
    sg = Cluster("AWS Security Group")
    tabl = Tableau("Tableau Users")
    salesforce = Mssql("Salesforce Database")

    with vpc:
        with Cluster("Server Security Group"):
            ec2 = EC2("ETL Worker")

        with Cluster("Database Security Group"):
            rds = RDS("Database")
            rds << S3("Database Backups")

        ec2 >> Edge(color="grey") >> rds

    tabl >> Edge(color="grey") >> rds
    salesforce << Edge(color="grey") >> ec2
