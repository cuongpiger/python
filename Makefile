create-env:
	@./cmd/commands.sh create_virtual_env

generate-calculator-protobuf:
	@./cmd/commands.sh generate_calculator_protobuf

install-deps:
	@./cmd/commands.sh install_dependencies

delete-env:
	@./cmd/commands.sh delete_virtual_env
	
run-server:
	@./cmd/commands.sh run_server

run-client:
	@./cmd/commands.sh run_client