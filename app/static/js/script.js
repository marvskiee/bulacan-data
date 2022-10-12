function UserForm() {
  //   year and section
  this.sectionSelect = document.querySelector("#section");
  this.yearSelect = document.querySelector("#year");
  //   province and municipality
  this.provinceSelect = document.querySelector("#province");
  this.municipalitySelect = document.querySelector("#municipality");
}
UserForm.prototype.init = function () {
  //   this.sectionSelect.document.addEventListener("onchange", () => this.changeForm(this));
  this.yearSelect?.addEventListener("change", () => this.changeSection(this));
  this.provinceSelect?.addEventListener("change", () =>
    this.changeMunicipality(this)
  );
};
UserForm.prototype.changeSection = function () {
  let yearVal = this.yearSelect.value;
  let thirdLayout = `
    <option value="A-G1, A-G2">
        A-G1, A-G2</option>
    <option value="B-G1, B-G2">
        B-G1, B-G2</option>
    <option value="C-G1, C-G2">
        C-G1, C-G2</option>
    <option value="D-G1, D-G2">
        D-G1, D-G2</option>
    <option value="E-G1, E-G2">
        E-G1, E-G2</option>
    <option value="F- G1, F-G2">
        F- G1, F-G2</option>
    <option value="G-G1, G-G2">
        G-G1, G-G2</option>
    <option value="H-G1, H-G2">
        H-G1, H-G2</option>
    <option value="I-G1, I-G2">
        I-G1, I-G2</option>
    <option value="J-G1, J-G2">
        J-G1, J-G2
    </option>
  `;
  let fourthLayout = `
    <option value="A">A</option>
    <option value="B">B</option>
    <option value="C">C</option>
    <option value="D">D</option>
    <option value="E">E</option>
    <option value="F">F</option>
    <option value="G">G</option>
    <option value="H">H</option>
    <option value="I">I</option>
    <option value="J">J</option>
    <option value="K">K</option>
    <option value="L">L</option>
    <option value="M">M</option>
    <option value="N">N</option>
    <option value="O">O</option>
    <option value="P">P</option>
    <option value="Q">Q</option>
    <option value="R">R</option>
    <option value="S">S</option>`;
  if (yearVal === "3rd Year") {
    this.sectionSelect.innerHTML = thirdLayout;
  } else {
    this.sectionSelect.innerHTML = fourthLayout;
  }
};
UserForm.prototype.changeMunicipality = function () {
  let bulacanLayout = `<option value="Angat">
    Angat
</option>
<option value="Balagtas">
    Balagtas
</option>
<option value="Baliwag">
    Baliwag
</option>
<option value="Bocaue">
    Bocaue
</option>
<option value="Bulakan">
    Bulakan
</option>
<option value="Bustos">
    Bustos
</option>
<option value="Calumpit">
    Calumpit
</option>
<option value="Dona Remedios Trinidad">
    Dona Remedios Trinidad
</option>
<option value="Guiguinto">
    Guiguinto
</option>
<option value="Hagonoy">
    Hagonoy
</option>
<option value="Malolos">
    Malolos
</option>
<option value="Marilao">
    Marilao
</option>
<option value="Meycauayan">
    Meycauayan
</option>
<option value="Norzagaray">
    Norzagaray
</option>
<option value="Obando">
    Obando
</option>
<option value="Pandi">
    Pandi
</option>
<option value="Paombong">
    Paombong
</option>
<option value="Plaridel">
    Plaridel
</option>
<option value="Pulilan">
    Pulilan
</option>
<option value="San Ildefonso">
    San Ildefonso
</option>
<option value="San Jose Del Monte">
    San Jose Del Monte
</option>
<option value="San Miguel">
    San Miguel
</option>
<option value="San Rafael">
    San Rafael
</option>
<option value="Santa Maria">
    Santa Maria
</option>
`;
  let pampangaLayout = `
<option value="Angeles City">
    Angeles City
</option>
<option value="Apalit">
    Apalit
</option>
<option value="Arayat">
    Arayat
</option>
<option value="Bacolor">
    Bacolor
</option>
<option value="Candaba">
    Candaba
</option>
<option value="Floridablanca">
    Floridablanca
</option>
<option value="Guagua">
    Guagua
</option>
<option value="Lubao">
    Lubao
</option>
<option value="Mabalacat">
    Mabalacat
</option>
<option value="Macabebe">
    Macabebe
</option>
<option value="Magalang">
    Magalang
</option>
<option value="Masantol">
    Masantol
</option>
<option value="Mexico">
    Mexico
</option>
<option value="Minalin">
    Minalin
</option>
<option value="Porac">
    Porac
</option>
<option value="San Fernando">
    San Fernando
</option>
<option value="San Luis">
    San Luis
</option>
<option value="San Simon">
    San Simon
</option>
<option value="Santa Ana">
    Santa Ana
</option>
<option value="Santa Rita">
    Santa Rita
</option>
<option value="Santo Tomas">
    Santo Tomas
</option>
<option value="Sasmuan">
    Sasmuan
</option>`;
  if (this.provinceSelect.value == "Bulacan") {
    this.municipalitySelect.innerHTML = bulacanLayout;
  } else {
    this.municipalitySelect.innerHTML = pampangaLayout;
  }
};
const userForm = new UserForm();
userForm.init();
