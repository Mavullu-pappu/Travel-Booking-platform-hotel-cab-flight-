
const role = document.getElementById("role");

const companyGroup = document.getElementById("company-group");
const companyName = document.getElementById("company_name");

const providerTypeGroup =
    document.getElementById("provider-type-group");

const providerType =
    document.getElementById("provider_type");

role.addEventListener("change", function () {

    const isProvider = this.value === "Provider";

    companyGroup.style.display =
        isProvider ? "block" : "none";

    providerTypeGroup.style.display =
        isProvider ? "block" : "none";

    companyName.required = isProvider;
    providerType.required = isProvider;

    if (!isProvider) {
        companyName.value = "";
        providerType.value = "";
    }
});
