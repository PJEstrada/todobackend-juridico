node {
	checkout scm
	try{
		stage 'Run unit/integration tests'
		sh 'make test'

		stage 'Build application artifacts'
		sh 'make build'

		stage 'Create release environment and run acceptance tests'
		sh 'make release'

		stage 'tag and publish release image'
		sh 'make tag latest \$(git rev-parse --short HEAD) \$(git tag --points-at HEAD)'
		sh 'make buildtag master \$(git tag --points-at HEAD)'
		withEnv(["DOCKER_USER=${DOCKER_USER}",
				 "DOCKER_PASSWORD=${DOCKER_PASSWORD}",
				 "DOCKER_EMAIL=${DOCKER_EMAIL}"]){
			sh 'make login'
			sh 'make publish'
		 }

        stage 'Deploy release'
        sh "printf \$(git rev-parse --short HEAD) > tag.tmp"
        def imageTag = readFile 'tag.tmp'
        build job: DEPLOY_JOB, parameters: [[
            $class: 'StringParameterValue',
            name: 'IMAGE_TAG',
            value: 'pjestrada/todobackend:' + imageTag
		]]

	}
	finally{
		stage 'Clean up'
		sh 'make clean'
		stage 'Collect test reports'
		sh 'make logout'
	}
}
