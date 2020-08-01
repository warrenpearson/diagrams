from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3


with Diagram("Example Infrastructure", direction="TB"):
    vpc = Cluster("Cloud")

    with vpc:
        ELB("Load Balancer") >> [EC2("API instance 1"),
            EC2("API instance 2")] >> RDS("database") << S3("db backups")
