package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strings"
)

// SETTING is struct
type SETTING struct {
	GithubCom     string   `json:"github.com"`        // Up to 2 layers above
	GolangOrg     string   `json:"golang.org"`        // Up one layer
	IgnoreFolders []string `json:"ignoreFolderNames"` // Ignored folders.
	StandardPkgs  string   `json:"standardpkgs"`      // Up one layer
}

func main() {
	var args []string
	var all bool
	var standard bool
	var help bool
	flag.BoolVar(&all, "all", false, "Show installed and standard packages.")
	flag.BoolVar(&standard, "standard", false, "Show only standard packages.")
	flag.BoolVar(&help, "h", false, "Show help of 'listpkgs' options.")
	flag.Parse()
	args = flag.Args()

	if help {
		flag.PrintDefaults()
		return
	}

	if len(args) > 0 && args[0] == "listpkgs" {
		// read JSON
		bytes, err := ioutil.ReadFile("listpkgs.json")
		if err != nil {
			log.Fatal(err)
		}
		// decode JSON
		var settings SETTING
		if err := json.Unmarshal(bytes, &settings); err != nil {
			log.Fatal(err)
		}

		if all {
			if settings.StandardPkgs == "" || settings.GithubCom == "" || settings.GolangOrg == "" {
				log.Fatal("Set 'standardpkgs', 'github.com' and 'golang.org' in listpkg.json.")
			}
		} else if standard {
			if settings.StandardPkgs == "" {
				log.Fatal("Set 'standardpkgs' in listpkg.json.")
			}
		} else {
			if settings.GithubCom == "" {
				log.Fatal("Set 'github.com' in listpkg.json.")
			}

		}

		if !standard {
			if strings.Contains(settings.GithubCom, "${") { // regexp.MustCompile(`/$\{.+?\}/`).MatchString(settings.GithubCom)
				settings.GithubCom = replaceEnvs(settings.GithubCom)
			}

			fmt.Println("Installed")
			pkgs := getPkgNames(settings.GithubCom, settings.IgnoreFolders, 1)
			for projectName := range pkgs {
				fmt.Println(" ├─ " + projectName)
				for _, pkgName := range pkgs[projectName] {
					fmt.Println(" │   ├─ " + pkgName)
				}
			}
		}

		if all || standard {
			if strings.Contains(settings.StandardPkgs, "${") { // regexp.MustCompile(`/$\{.+?\}/`).MatchString(settings.StandardPkgs)
				settings.StandardPkgs = replaceEnvs(settings.StandardPkgs)
			}

			fmt.Println("Standard")
			pkgs := getPkgNames(settings.StandardPkgs, settings.IgnoreFolders, 0)
			for projectName := range pkgs {
				fmt.Println(" ├─ " + projectName)
				for _, pkgName := range pkgs[projectName] {
					fmt.Println(" │   ├─ " + pkgName)
				}
			}
		}

		if all {
			if strings.Contains(settings.GolangOrg, "${") { // regexp.MustCompile(`/$\{.+?\}/`).MatchString(settings.GolangOrg)
				settings.GolangOrg = replaceEnvs(settings.GolangOrg)
			}

			fmt.Println("Tools")
			pkgs := getPkgNames(settings.GolangOrg, settings.IgnoreFolders, 0)
			for projectName := range pkgs {
				fmt.Println(" ├─ " + projectName)
				for _, pkgName := range pkgs[projectName] {
					fmt.Println(" │   ├─ " + pkgName)
				}
			}
		}
	}
}

func getPkgNames(path string, ignoreFolders []string, n int) map[string][]string {
	var pkgs = make(map[string][]string)
	folders, err := ioutil.ReadDir(path)
	if err != nil {
		log.Fatal(err)
	}

	switch n {
	case 0:
		splitted := strings.Split(path, "\\")
		projectName := splitted[len(splitted)-1]
		for _, f := range folders {
			if f.IsDir() { // read only folder-name
				pkgs[projectName] = append(pkgs[projectName], f.Name())
			}
		}
	default:
		for _, f := range folders {
			if f.IsDir() {
				// folders settid "ignoreFolderNames" are ignored.
				if existStrInArray(ignoreFolders, f.Name()) {
					continue
				}
				pkgs = merge(pkgs, getPkgNames(path+"\\"+f.Name(), ignoreFolders, (n-1)))
			}
		}
	}
	return pkgs
}

func existStrInArray(array []string, value string) bool {
	for _, v := range array {
		// If there is a same value. return true.
		if value == v {
			return true
		}
	}
	return false
}

func merge(arr1 map[string][]string, arr2 map[string][]string) map[string][]string {
	var new = make(map[string][]string)
	for k := range arr1 {
		for _, v := range arr1[k] {
			new[k] = append(new[k], v)
		}
	}
	for k := range arr2 {
		for _, v := range arr2[k] {
			new[k] = append(new[k], v)
		}
	}
	return new
}

func replaceEnvs(path string) string {
	// Get words between "${" and "}"
	envVals := getInner2Array(path, "${?}")
	for j := 0; j < len(envVals); j++ {
		// Replace Environment-value to absolute-path
		path = strings.Replace(path, "${"+envVals[j]+"}", os.Getenv(envVals[j]), -1)
	}
	return path
}

func getInner2Array(str string, enclosure string) []string {
	// Divide "enclosure" into opening and closing of enclosure by "?"
	ens := strings.Split(enclosure, "?")
	// Divide "str" by opening of "enclosure", and get the latter.
	result := strings.Split(str, ens[0])
	for i := 0; i < len(result); i++ {
		// Divide "result[i]" by closing of "enclosure", and get the former.
		result[i] = strings.Split(result[i], ens[1])[0]
	}
	return result
}
