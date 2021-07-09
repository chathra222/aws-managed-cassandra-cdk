from aws_cdk import core as cdk
import aws_cdk.aws_cassandra as cassandra


class cassandraCdkStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ks = cassandra.CfnKeyspace(
            self, "MycassandraKeySpace", keyspace_name="MycassandraKeySpace"
        )
        cassandra.CfnTable(
            self,
            "CustomerTable",
            table_name="Customer",
            keyspace_name="MycassandraKeySpace",
            regular_columns=[
                cassandra.CfnTable.ColumnProperty(
                    column_name="name",
                    column_type="varchar",
                ),
                cassandra.CfnTable.ColumnProperty(
                    column_name="country",
                    column_type="varchar",
                ),
                cassandra.CfnTable.ColumnProperty(
                    column_name="email", column_type="varchar"
                ),
            ],
            partition_key_columns=[
                cassandra.CfnTable.ColumnProperty(
                    column_name="id", column_type="varchar"
                )
            ],
        ).add_depends_on(ks)
