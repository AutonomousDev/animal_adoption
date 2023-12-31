import {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonContent,
    IonButton,
    IonSelect,
    IonSelectOption,
    IonItem,
    IonIcon,
    useIonAlert,
    IonDatetimeButton,
    IonModal,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonDatetime,
    useIonRouter,
} from "@ionic/react";
import React from "react";
import { logOutOutline } from "ionicons/icons";
import { BASE } from "../constants";

const Search: React.FC = () => {
    const router = useIonRouter();

    const doLogout = () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ refresh: localStorage.getItem("refresh") }),
        };

        // There is no await here because I don't care about the result.
        fetch(`${BASE}/token/blacklist/`, requestOptions);

        localStorage.setItem("token", "");
        localStorage.setItem("refresh", "");
        router.push("/", "root", "replace");
    };

    const [availabilities, setAvailabilities] = React.useState([]);
    const [availabilitiesState, setAvailabilitiesState] = React.useState([]);
    const [breeds, setBreeds] = React.useState([]);
    const [breedsState, setBreedsState] = React.useState([]);
    const [dispositions, setDispositions] = React.useState([]);
    const [dispositionsState, setDispositionsState] = React.useState([]);
    // const [sizes, setSizes] = React.useState([]);
    // const [sizesState, setSizesState] = React.useState("");
    const [species, setSpecies] = React.useState([]);
    const [speciesState, setSpeciesState] = React.useState([]);

    //Used for setting starting dates of pickers:
    let today = new Date();

    const [endDate, setEndDate] = React.useState(
        today.toISOString().slice(0, 10)
    );

    today = new Date();
    today.setFullYear(today.getFullYear() - 5);

    const [startDate, setStartDate] = React.useState(
        today.toISOString().slice(0, 10)
    );

    const [animalList, setAnimalList] = React.useState([]);

    const [presentAlert] = useIonAlert();

    const getOptions = async () => {
        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
        };

        const response = await fetch(`${BASE}/animal-options/`, requestOptions);

        if (response.ok) {
            const data = await response.json();
            setAvailabilities(data.availabilities);
            setSpecies(data.species);
            setDispositions(data.dispositions);
            setBreeds(data.breeds);
            // console.log(data);
        } else {
            presentAlert({
                header: "Error",
                subHeader: "",
                message: "Unable to fetch filter options.",
                buttons: ["OK"],
            });
        }
    };

    const handleSubmit = async () => {
        //Options accepted by filter view: age, availability, availability_id, breed, breed_id, date_entered, disposition, id, image, name, news, shelter, shelter_id, size, size_id, species, species_id, views

        let url = `${BASE}/animals/?`;
        let urlSuffixes = [];

        if (availabilitiesState && availabilitiesState.length > 0) {
            for (let i = 0; i < availabilitiesState.length; i++) {
                urlSuffixes.push(`availability=${availabilitiesState[i]}`);
            }
        }

        if (speciesState && speciesState.length > 0) {
            for (let i = 0; i < speciesState.length; i++) {
                urlSuffixes.push(`species=${speciesState[i]}`);
            }
        }

        if (dispositionsState && dispositionsState.length > 0) {
            for (let i = 0; i < dispositionsState.length; i++) {
                urlSuffixes.push(`disposition=${dispositionsState[i]}`);
            }
        }

        if (breedsState && breedsState.length > 0) {
            for (let i = 0; i < breedsState.length; i++) {
                urlSuffixes.push(`breed=${breedsState[i]}`);
            }
        }

        if (startDate && startDate !== "") {
            urlSuffixes.push(`date_entered_after=${startDate}`);
        }

        if (endDate && endDate !== "") {
            urlSuffixes.push(`date_entered_before=${endDate}`);
        }

        url += urlSuffixes.join("&");

        // console.log(url);

        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                Authorization: `Bearer ${token}`,
            },
        };

        const response = await fetch(url, requestOptions);

        if (response.ok) {
            const data = await response.json();
            // console.log(data);
            setAnimalList(data);
        } else {
            presentAlert({
                header: "Error",
                subHeader: "",
                message: "Unable to get results.",
                buttons: ["OK"],
            });
        }
    };

    React.useEffect(() => {
        getOptions();
    }, []);

    return (
        <IonContent>
            <IonHeader>
                <IonToolbar>
                    <IonTitle>Search for Matches</IonTitle>
                    <IonButton type="submit" onClick={doLogout} slot="end">
                        Logout{" "}
                        <IonIcon slot="end" icon={logOutOutline}></IonIcon>
                    </IonButton>
                </IonToolbar>
            </IonHeader>
            <IonCard>
                <IonCardContent>
                    <h3>Availability</h3>
                    <IonItem>
                        <IonSelect
                            aria-label="availabilities"
                            placeholder="Select all availabilities to include"
                            interface="popover"
                            multiple={true}
                            onIonChange={(e) =>
                                setAvailabilitiesState(e.detail.value)
                            }
                        >
                            {availabilities.map((availability) => (
                                <IonSelectOption value={availability.id}>
                                    {availability.availability}
                                </IonSelectOption>
                            ))}
                        </IonSelect>
                    </IonItem>
                </IonCardContent>
                <IonCardContent>
                    <h3>Species</h3>
                    <IonItem>
                        <IonSelect
                            aria-label="species"
                            placeholder="Select all species to include"
                            interface="popover"
                            multiple={true}
                            onIonChange={(e) => setSpeciesState(e.detail.value)}
                        >
                            {species.map((specie) => (
                                <IonSelectOption value={specie.id}>
                                    {specie.name}
                                </IonSelectOption>
                            ))}
                        </IonSelect>
                    </IonItem>
                </IonCardContent>
                <IonCardContent>
                    <h3>Dispositions</h3>
                    <IonItem>
                        <IonSelect
                            aria-label="dispositions"
                            placeholder="Select all dispositions to include"
                            interface="popover"
                            multiple={true}
                            onIonChange={(e) =>
                                setDispositionsState(e.detail.value)
                            }
                        >
                            {dispositions.map((disposition) => (
                                <IonSelectOption value={disposition.id}>
                                    {disposition.disposition}
                                </IonSelectOption>
                            ))}
                        </IonSelect>
                    </IonItem>
                </IonCardContent>

                <IonCardContent>
                    <h3>Breeds</h3>
                    <IonItem>
                        <IonSelect
                            aria-label="breeds"
                            placeholder="Select all breeds to include"
                            interface="popover"
                            multiple={true}
                            onIonChange={(e) => setBreedsState(e.detail.value)}
                        >
                            {breeds.map((breed) => (
                                <IonSelectOption value={breed.id}>
                                    {breed.name}
                                </IonSelectOption>
                            ))}
                        </IonSelect>
                    </IonItem>
                </IonCardContent>

                <IonCardContent>
                    Posted from
                    <IonDatetimeButton
                        id="datetime-button"
                        datetime="datetime"
                    ></IonDatetimeButton>
                    <IonModal keepContentsMounted={true}>
                        <IonDatetime
                            id="datetime"
                            presentation="date"
                            value={startDate}
                            onIonChange={(e) => setStartDate(e.detail.value)}
                        ></IonDatetime>
                    </IonModal>{" "}
                    to{" "}
                    <IonDatetimeButton
                        id="datetime-button2"
                        datetime="datetime2"
                    ></IonDatetimeButton>
                    <IonModal keepContentsMounted={true}>
                        <IonDatetime
                            id="datetime2"
                            presentation="date"
                            value={endDate}
                            onIonChange={(e) => setEndDate(e.detail.value)}
                        ></IonDatetime>
                    </IonModal>
                </IonCardContent>
                <IonButton expand="block" onClick={handleSubmit}>
                    Find matches
                </IonButton>
            </IonCard>
            {animalList.map((animal, index) => (
                <IonCard id={index + "animalcard"}>
                    <IonCardHeader>
                        <IonCardTitle>{animal.name}</IonCardTitle>
                    </IonCardHeader>
                    <IonCardContent>
                        {animal.image ? (
                            <IonCardContent>
                                <img
                                    max-width="100"
                                    height="100"
                                    src={animal.image}
                                />
                            </IonCardContent>
                        ) : (
                            ``
                        )}

                        {animal.availability.availability ? (
                            <p>
                                Availability: {animal.availability.availability}
                            </p>
                        ) : (
                            ``
                        )}

                        {animal.species && animal.species.name ? (
                            <p>Species: {animal.species.name}</p>
                        ) : (
                            ``
                        )}
                    </IonCardContent>
                    <IonModal trigger={index + "animalcard"}>
                        <IonHeader>
                            <IonToolbar>
                                <IonTitle>{animal.name}</IonTitle>
                            </IonToolbar>
                        </IonHeader>
                        <IonContent className="ion-padding">
                            {animal.image ? (
                                <img
                                    max-width="300"
                                    height="300"
                                    src={animal.image}
                                />
                            ) : (
                                ``
                            )}

                            {animal.availability.availability ? (
                                <p>
                                    Availability:{" "}
                                    {animal.availability.availability}
                                </p>
                            ) : (
                                ``
                            )}

                            {animal.species && animal.species.name ? (
                                <p>Species: {animal.species.name}</p>
                            ) : (
                                ``
                            )}

                            {animal.breed && animal.breed.name ? (
                                <p>Breed: {animal.breed.name}</p>
                            ) : (
                                ``
                            )}

                            {animal.disposition ? <p>Dispositions:</p> : ``}
                            <ul>
                                {animal.disposition.map((disposition) => (
                                    <li>{disposition.disposition}</li>
                                ))}
                            </ul>

                            {animal.age ? <p>Age: {animal.age}</p> : ``}

                            {animal.size && animal.size.name ? (
                                <p>Size: {animal.size.name}</p>
                            ) : (
                                ``
                            )}

                            {animal.shelter && animal.shelter.name ? (
                                <p>Shelter: {animal.shelter.name}</p>
                            ) : (
                                ``
                            )}

                            {animal.date_entered ? (
                                <p>
                                    Date entered:{" "}
                                    {animal.date_entered.slice(0, 10)}
                                </p>
                            ) : (
                                ``
                            )}
                        </IonContent>
                    </IonModal>
                </IonCard>
            ))}
        </IonContent>
    );
};

export default Search;
